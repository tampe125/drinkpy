import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT


class Pumps:
    def __init__(self):
        self.shield = Adafruit_MotorHAT(addr=0x60)
        shield = self.shield

        # We are using a function detached from object instance so we can save memory
        def turnOffMotors():
            """
            Register our function to stop all motors on exit
            """
            shield.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
            shield.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
            shield.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
            shield.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

        atexit.register(turnOffMotors)
