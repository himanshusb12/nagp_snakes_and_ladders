from math import ceil
from json import load

import matplotlib.pyplot as plt
from pandas import option_context, read_json
from seaborn import lineplot, countplot

from shared.constants import GAME_DATA_FILE


class GameStats:
    def __init__(self):
        """
        Provides visual data of the last saved game for analysis.
        """
        self.game_json = None
        try:
            with open(GAME_DATA_FILE) as file:
                self.game_json = load(file)
        except FileNotFoundError:
            print('No game data file found. Please play a game to save a new one.')
        except Exception:
            print('Some error occurred while reading the game data file.')

    def load_menu(self):
        """
        Loads menu for statistical analysis.
        """
        while True:
            print('\t1. Show as a plot')
            print('\t2. Print directly on console')
            print('\t3. Exit')
            user_selection = input('\nEnter your choice (1-3): ')
            print()
            if user_selection == '1':
                self.load_graphs()
            elif user_selection == '2':
                self.pretty_print()
            elif user_selection == '3':
                exit()
            else:
                print('Select an available choice between 1 and 3')

    def load_graphs(self):
        """
        Loads menu to load different plots based on user choice.
        """
        rolls_data = read_json(self.game_json['rolls'])
        moves_data = read_json(self.game_json['moves'])
        moves_data.index += 1
        rolls_data.index += 1
        while True:
            print('\t1. Show all players game play as line plot')
            print('\t2. Show all players dice rolls as count plot')
            print('\t3. Return')
            user_selection = input('\nEnter your choice (1-3): ')
            print()
            if user_selection == '1':
                figure, axes = plt.subplots(ncols=1)
                figure.suptitle('GamePlay Line Plot')
                moves_line_plot = lineplot(data=moves_data, ax=axes)
                moves_line_plot.set(xlabel='Number of turns', ylabel='Position on board')
                plt.show()
            elif user_selection == '2':
                total = len(rolls_data.columns)
                num_rows = ceil(total / 2)
                figure, axes = plt.subplots(num_rows, 2, constrained_layout=True)
                figure.suptitle('Dice Number Occurrence')
                for i, axis in enumerate(axes.flatten(), 1):
                    if i > total:
                        figure.delaxes(axis)
                        break
                    plot = countplot(x=rolls_data[f'Player {i}'], ax=axis, palette="Set3")
                    plot.set_title(f'Player {i}')
                    plot.set(xlabel='Number on dice', ylabel='Count')
                plt.show()
            elif user_selection == '3':
                return
            else:
                print('Select an available choice between 1 and 3')

    def pretty_print(self):
        rolls_data = read_json(self.game_json['rolls'])
        moves_data = read_json(self.game_json['moves'])
        moves_data.index += 1
        rolls_data.index += 1
        with option_context('display.max_rows', None, 'display.max_columns', None):
            print("\t\tPlayers' position data")
            print(moves_data)
            print("\n\t\tPlayers' dice roll data")
            print(rolls_data)
            print()