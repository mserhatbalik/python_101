from random import choice

class Lottery:
    def __init__(self):
        self.number_letter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e"]
        self.winner_list = []

    def hitbig(self):
        for _ in range(0, 4):
            self.winner_list.append(choice(self.number_letter_list))
        return self.winner_list

