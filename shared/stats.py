from json import load

import matplotlib.pyplot as plt
from pandas import read_json
from seaborn import lineplot, scatterplot

from shared.constants import GAME_DATA_FILE


def load_graphs(game_json):
    rolls_data = read_json(game_json['rolls'])
    moves_data = read_json(game_json['moves'])
    moves_data.index += 1
    rolls_data.index += 1
    while True:
        print('\t1. Show line plots')
        print('\t2. Show scatter plots')
        print('\t3. Exit')
        user_selection = input('\nEnter your choice (1-3): ')
        print()
        if user_selection == '1':
            figure, axes = plt.subplots(ncols=2)
            figure.suptitle('GamePlay Line Plot')
            moves_line_plot = lineplot(data=moves_data, ax=axes[0])
            moves_line_plot.set(xlabel='Number of turns', ylabel='Position on board')
            rolls_line_plot = lineplot(data=rolls_data, ax=axes[1])
            rolls_line_plot.set(xlabel='Number of turns', ylabel='Dice Roll')
            plt.show()
        elif user_selection == '2':
            figure, axes = plt.subplots(ncols=2)
            figure.suptitle('GamePlay Scatter Plot')
            moves_line_plot = scatterplot(data=moves_data, ax=axes[0])
            moves_line_plot.set(xlabel='Number of turns', ylabel='Position on board')
            rolls_line_plot = scatterplot(data=rolls_data, ax=axes[1])
            rolls_line_plot.set(xlabel='Number of turns', ylabel='Dice Roll')
            plt.show()
        elif user_selection == '3':
            return
        else:
            print('Select an available choice between 1 and 3')


def load_last_game():
    while True:
        print('\t1. Show as a graph')
        print('\t2. Print directly on console')
        print('\t3. Exit')
        user_selection = input('\nEnter your choice (1-3): ')
        print()
        try:
            with open(GAME_DATA_FILE) as file:
                game_json = load(file)
        except FileNotFoundError:
            print('No game data file found. Please play a game to save a new one.')
            return
        except Exception:
            print('Some error occurred while reading the game data file.')
            return
        if user_selection == '1':
            load_graphs(game_json)
        elif user_selection == '2':
            for key, data in game_json.items():
                print(key)
                print(data, '\n')
        elif user_selection == '3':
            exit()
        else:
            print('Select an available choice between 1 and 3')