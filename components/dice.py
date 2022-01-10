from random import randint


class Dice:
    def __init__(self, min_num=1, max_num=6):
        """
        Initializes a dice to play with.

        Parameters
        ----------
        min_num: int
            Minimum number to get on the dice
        max_num: int
            Maximum number to get on the dice, also getting the maximum number will reward a one more dice roll
        """
        self.min_num = min_num
        self.max_num = max_num
        print(f'>>>> Setting up a dice with {self.min_num} and {self.max_num} as minimum and maximum numbers to get,'
              f' also getting a {self.max_num} will reward one more dice roll')

    def roll(self):
        """
        Generates a random number between minimum and maximum dice numbers.

        Returns
        -------
        int
        """
        return randint(self.min_num, self.max_num)

    def got_one_more_roll(self, rolled_number):
        """
        Checks whether one more dice roll is rewarded or not.

        Parameters
        ----------
        rolled_number: int
            Least recent number got on the dice roll

        Returns
        -------
        bool
        """
        if rolled_number == self.max_num:
            return True
        return False
