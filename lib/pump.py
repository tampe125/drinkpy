import atexit
import json


class Pumps:
    def __init__(self, commands, shield):
        self.shield = shield
        local_shield = self.shield

        # We are using a function detached from object instance so we can save memory
        def turnOffMotors():
            """
            Register our function to stop all motors on exit
            """
            # No need to load the class just for the constants
            # FORWARD = 1 BACKWARD = 2 BRAKE = 3 RELEASE = 4
            local_shield.getMotor(1).run(4)
            local_shield.getMotor(2).run(4)
            local_shield.getMotor(3).run(4)
            local_shield.getMotor(4).run(4)

        atexit.register(turnOffMotors)

        try:
            self.commands = json.loads(commands)
        except ValueError:
            # TODO Throw a different error and stop the execution
            pass
