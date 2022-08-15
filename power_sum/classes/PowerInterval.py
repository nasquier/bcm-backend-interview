class PowerInterval:
    def __init__(self, start: int, end: int, power: int):
        self.start = start
        self.end = end
        self.power = power

    def get_dict(self):
        return {"start": self.start, "end": self.end, "power": self.power}
