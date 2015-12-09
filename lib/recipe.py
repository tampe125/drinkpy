import atexit
import json
from threading import Timer
from time import sleep
from lib.pump import Pump


class Recipe:
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
            self.commands = json.loads(commands).get('stack')
        except ValueError:
            raise RuntimeError("Invalid command, stopping")

    def run(self):
        first = Pump(self.shield)
        thread_1 = Timer(1, first.run, args=self.commands)
        # thread_2 = Timer(1, Pump(self.shield).run(self.commands))

        for process in [thread_1, ]:
            process.daemon = True
            process.start()

        # Let threads run
        try:
            while 1:
                sleep(0.5)
        except KeyboardInterrupt:
            pass
