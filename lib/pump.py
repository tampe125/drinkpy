

class Pump:
    def __init__(self, shield):
        self.shield = shield
        self.current = None

    def run(self, stack):
        if not self.current:
            self.current = stack.pop()
