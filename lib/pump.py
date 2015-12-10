from time import sleep, time


class Pump:
    def __init__(self, shield, stack):
        self.shield = shield
        self.current = None
        self.start = 0
        self.end = 0
        self.stack = stack

    def run(self):
        while 1:
            # If I don't have a current item, let's pop the stack and fire up the motor
            if not self.current:
                try:
                    self.current = self.stack.pop()
                except IndexError:
                    break

                num_motor = int(self.current.keys()[0])
                interval = self.current.values()[0]

                print "Starting motor " + str(num_motor) + " for " + str(interval) + " seconds"

                motor = self.shield.getMotor(num_motor)
                motor.setSpeed(200)
                motor.run(1)

                self.start = time()
                self.end = self.start + interval

            sleep(1)

            if time() >= self.end:
                num_motor = int(self.current.keys()[0])
                print "Stopping motor " + str(num_motor)
                self.shield.getMotor(num_motor).run(4)

                self.start = 0
                self.end = 0
                self.current = None
