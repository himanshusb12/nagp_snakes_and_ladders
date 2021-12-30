from random import randint


class Dice:
    def __init__(self, min_num=1, max_num=6):
        self.min_num = min_num
        self.max_num = max_num

    def roll(self):
        return randint(self.min_num, self.max_num)
