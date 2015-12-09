

class FakeHat:
    def __init__(self):
        self.num = 0
        pass

    def getMotor(self, num):
        self.num = num

        return self

    def run(self, command):
        print "Motor " + str(self.num) + " set command: " + str(command)

    def setSpeed(self, speed):
        print "Motor " + str(self.num) + " set speed: " + str(speed)
