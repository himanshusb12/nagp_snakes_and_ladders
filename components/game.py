from components.board import Board
from components.dice import Dice
from components.stats import GameStats
from shared.utils import enter_a_valid_number_or_default
from shared.constants import DEFAULT_BOARD, DEFAULT_DICE


class Game:
    def __init__(self):
        self.board = None
        self.dice = None
        self.num_of_players = 0

    def play(self):
        """
        Game play on the board.
        """
        while True:
            for player in range(1, self.num_of_players + 1):
                print(f"\n>>>> Player {player}'s turn")
                while True:
                    roll = input('\tPress enter to roll a dice ')
                    if roll == '':
                        dice_roll = self.dice.roll()
                        print(f'>>>> Player {player} rolled a dice and got {dice_roll}')
                        player_moved = self.board.move_player(player, dice_roll)
                        if not self.dice.got_one_more_roll(dice_roll) or not player_moved:
                            break
                        print(f'>>>> GREAT! One more turn for Player {player}')
                    else:
                        print('>>>> Please roll a dice to move forward')
                if self.board.check_for_victory(player):
                    self.board.save_the_play()
                    return

    def set_board(self, custom=False):
        """
        Sets the board to play the game.

        Parameters
        ----------
        custom: bool
            Want to set the board manually
        """
        if custom:
            rows, columns = self.get_num_of_rows_and_columns()
            self.board = Board(num_of_players=self.num_of_players, rows=rows, columns=columns)
            self.board.manual_setup()
        else:
            self.board = Board(num_of_players=self.num_of_players)
            self.board.default_setup()

    def set_dice(self, custom=False):
        """
        Sets the dice to play the game.

        Parameters
        ----------
        custom: bool
            Want to set the dice manually
        """
        if custom:
            min_num, max_num = self.get_min_and_max_for_dice()
            self.dice = Dice(min_num=min_num, max_num=max_num)
        else:
            self.dice = Dice()

    def set_num_of_players(self):
        """
        User prompt to set a valid number of players to start the game.
        """
        while True:
            try:
                num_of_players = int(input('\tQ. How many players want to play: '))
                if num_of_players < 2:
                    print('>>>> You need at least 2 players to play a game')
                    continue
                break
            except Exception:
                print('\t>>>> Enter a valid number of players')
        self.num_of_players = num_of_players

    @staticmethod
    def get_num_of_rows_and_columns():
        """
        User prompt to get valid number of rows and columns to set up a board.

        Returns
        -------
        (int, int)
            number of rows and columns for a board
        """
        rows = enter_a_valid_number_or_default('\tQ. How many rows you want on your board? ')
        if rows == 'default':
            rows = DEFAULT_BOARD['num_of_rows']
        cols = enter_a_valid_number_or_default('\tQ. How many columns you want on your board? ')
        if cols == 'default':
            cols = DEFAULT_BOARD['num_of_columns']
        return rows, cols

    @staticmethod
    def get_min_and_max_for_dice():
        """
        User prompt to get valid minimum and maximum values for a dice setup.

        Returns
        -------
        (int, int)
            min and max value on dice
        """
        min_num = enter_a_valid_number_or_default('\tQ. What should be the minimum number on dice? ')
        if min_num == 'default':
            min_num = DEFAULT_DICE['min']
        while True:
            max_num = enter_a_valid_number_or_default('\tQ. What should be the maximum number on dice? ')
            if max_num == 'default':
                max_num = DEFAULT_DICE['max']
            if max_num <= min_num:
                print('\t>>>> Maximum value should be greater than minimum value')
                continue
            break
        return min_num, max_num

    def load_menu(self):
        """
        Menu screen of the game
        """
        print('___________________________________________________________________________________________________________')
        print('\t\t\t\t\t SNAKES AND LADDERS \t\t\t\t\t\t\t\t')
        print('___________________________________________________________________________________________________________')
        while True:
            print('\n\t\t\t\t\t   ++++ Menu ++++ \t\t\t\t\t\t\t\t')
            print('\t1. Start a game')
            print('\t2. Configure and Play')
            print('\t3. Load last game statistics')
            print('\t4. Exit')
            user_selection = input('\nEnter your choice (1-4): ')
            print()

            if user_selection == '1':
                print('>>>> Starting a new game')
                self.set_num_of_players()
                self.set_board()
                self.set_dice()
                self.play()
                user_selection = input('\nWant to play again (y): ')
                if user_selection == 'y':
                    continue
                else:
                    break
            elif user_selection == '2':
                print('>>>> Configuring a new game')
                self.set_num_of_players()
                self.set_board(custom=True)
                self.set_dice(custom=True)
                self.play()
                user_selection = input('\nWant to play again (y): ')
                if user_selection == 'y':
                    continue
                else:
                    break
            elif user_selection == '3':
                print('>>>> Loading last game statistics')
                game_stats = GameStats()
                if game_stats.game_json is None:
                    continue
                game_stats.load_menu()
                break
            elif user_selection == '4':
                exit()
            else:
                print('>>>> Select an available choice between 1 and 4')