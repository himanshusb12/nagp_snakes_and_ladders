from components.board import Board
from components.dice import Dice
from shared.utils import enter_a_valid_number_or_default
from shared.stats import load_last_game
from shared.constants import DEFAULT_BOARD, DEFAULT_DICE


def play(board, dice, num_of_players):
    while True:
        for player in range(1, num_of_players + 1):
            print(f"\n>>>> Player {player}'s turn")
            while True:
                roll = input('\tPress enter to roll a dice ')
                if roll == '':
                    dice_roll = dice.roll()
                    print(f'>>>> Player {player} rolled a dice and got {dice_roll}')
                    player_moved = board.move_player(player, dice_roll)
                    if not dice.got_one_more_roll(dice_roll) or not player_moved:
                        break
                    print(f'>>>> GREAT! One more turn for Player {player}')
                else:
                    print('>>>> Please roll a dice to move forward')
            if board.check_for_victory(player):
                board.save_the_play()
                return


def get_num_of_players():
    while True:
        try:
            num_of_players = int(input('\tHow many players want to play: '))
            if num_of_players < 2:
                print('>>>> You need at least 2 players to play a game')
                continue
            break
        except:
            print('\t>>>> Enter a valid number of players')
    return num_of_players


def get_num_of_rows_and_columns():
    rows = enter_a_valid_number_or_default('How many rows you want on your board? ')
    if rows == 'default':
        rows = DEFAULT_BOARD['num_of_rows']
    cols = enter_a_valid_number_or_default('How many columns you want on your board? ')
    if cols == 'default':
        cols = DEFAULT_BOARD['num_of_columns']
    return rows, cols


def get_min_and_max_for_dice():
    min_num = enter_a_valid_number_or_default('What should be the minimum number on dice? ')
    if min_num == 'default':
        min_num = DEFAULT_DICE['min']
    max_num = enter_a_valid_number_or_default('What should be the maximum number on dice? ')
    if max_num == 'default':
        max_num = DEFAULT_DICE['max']
    return min_num, max_num


def load_menu():
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
            num_of_players = get_num_of_players()
            board = Board(num_of_players=num_of_players)
            board.default_setup()
            dice = Dice()
            play(board, dice, num_of_players)
            user_selection = input('\nWant to play again (y): ')
            if user_selection == 'y':
                continue
            else:
                break
        elif user_selection == '2':
            print('Configuring a new game')
            num_of_players = get_num_of_players()
            rows, columns = get_num_of_rows_and_columns()
            board = Board(num_of_players=num_of_players, rows=rows, columns=columns)
            board.manual_setup()
            min_num, max_num = get_min_and_max_for_dice()
            dice = Dice(min_num=min_num, max_num=max_num)
            play(board, dice, num_of_players)
            user_selection = input('\nWant to play again (y): ')
            if user_selection == 'y':
                continue
            else:
                break
        elif user_selection == '3':
            print('Loading last game statistics')
            load_last_game()
            break
        elif user_selection == '4':
            exit()
        else:
            print('Select an available choice between 1 and 4')


if __name__ == '__main__':
    load_menu()
