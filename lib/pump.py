from threading import Thread
from time import sleep, time


class Pump:
    def __init__(self, shield):
        self.shield = shield
        self.current = None
        self.start = 0
        self.end = 0

        # super(Thread, self).__init__(self)

    def execute(self, stack):
        while 1:
            # If I don't have a current item, let's pop the stack and fire up the motor
            if not self.current:
                try:
                    self.current = stack.pop()
                except IndexError:
                    break

                motor = self.current.keys()[0]
                interval = self.current.values()[0]

                print "Starting motor " + str(motor) + " for " + str(interval) + " seconds"

                # TODO Start the motor

                self.start = time()
                self.end = self.start + interval

            sleep(1)

            if time() >= self.end:
                print "Stopping motor " + str(self.current.keys()[0])
                # TODO Stop the motor

                self.start = 0
                self.end = 0
                self.current = None
