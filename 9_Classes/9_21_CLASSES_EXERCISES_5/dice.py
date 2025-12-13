from random import randint

class Dice:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        return randint(1, self.sides)

    def set_sides(self, sides):
        self.sides = sides