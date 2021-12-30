from components.board import Board
from components.dice import Dice
from shared.utils import enter_a_valid_number


def play(board, dice, num_of_players):
    while True:
        for player in range(1, num_of_players + 1):
            print(f">>>> Player {player}'s turn")
            while True:
                roll = input('\tPress enter to roll a dice: ')
                if roll == '':
                    dice_roll = dice.roll()
                    print(f'>>>> Player {player} rolled a dice and got {dice_roll}')
                    board.move_player(player, dice_roll)
                    if board.check_for_victory(player):
                        return
                    break
                else:
                    print('>>>> Please roll a dice to move forward')


def get_num_of_players():
    while True:
        try:
            num_of_players = int(input('\tHow many players want to play: '))
            if num_of_players < 2:
                print('>>>> You need at least 2 players to play a game')
                continue
            break
        except:
            print('>>>> Enter a valid number of players')
    return num_of_players


def get_num_of_rows_and_columns():
    rows = enter_a_valid_number('How many rows you want on your board? ')
    cols = enter_a_valid_number('How many columns you want on your board? ')
    return rows, cols


def load():
    print('___________________________________________________________________________________________________________')
    print('\t\t\t\t\t SNAKES AND LADDERS \t\t\t\t\t\t\t\t')
    print('___________________________________________________________________________________________________________')
    while True:
        print('\n\t\t\t\t\t   ++++ Menu ++++ \t\t\t\t\t\t\t\t')
        print('\t1. Start a game')
        print('\t2. Configure')
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
            dice = Dice()
            play(board, dice, num_of_players)
            user_selection = input('\nWant to play again (y): ')
            if user_selection == 'y':
                continue
            else:
                break
        elif user_selection == '3':
            print('Loading last game statistics')
            break
        elif user_selection == '4':
            exit()
        else:
            print('Select an available choice between 1 and 4')


if __name__ == '__main__':
    load()