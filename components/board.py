from json import dump

from numpy import append, array
from pandas import concat, DataFrame

from .ladder import Ladder
from .snake import Snake
from shared.exception import BoardException
from shared.utils import enter_a_valid_number
from shared.constants import DEFAULT_BOARD, GAME_DATA_FILE


class Board:
    def __init__(self, num_of_players, rows=10, columns=10):
        """
        Initializes a game board.

        Parameters
        ----------
        num_of_players: int
            Number of players
        rows: int
            Number of rows on the board, default value is 10 rows
        columns: int
            Number of columns on the board, default value is 10 columns
        """
        self.rows = rows
        self.columns = columns
        self.win_position = self.rows * self.columns
        self.ladders = {}
        self.snakes = {}
        self.player_positions = {f'Player {player}': array([0], dtype=int) for player in range(1, num_of_players + 1)}
        self.player_dice_rolls = {f'Player {player}': array([], dtype=int) for player in range(1, num_of_players + 1)}

    def add_ladder(self, bottom, top):
        """
        Adds a valid ladder on the board.

        Parameters
        ----------
        bottom: int
            Bottom position of the ladder
        top: int
            Top position of the ladder
        """
        ladder = Ladder(bottom=bottom, top=top)
        if self.__is_valid_ladder(ladder):
            self.ladders[bottom] = ladder

    def add_snake(self, mouth, tail):
        """
        Adds a valid snake on the board.

        Parameters
        ----------
        mouth: int
            Position of snake's mouth
        tail: int
            Position of snake's tail
        """
        snake = Snake(mouth=mouth, tail=tail)
        if self.__is_valid_snake(snake):
            self.snakes[mouth] = snake

    def __is_valid_ladder(self, ladder):
        """
        Validates a given ladder.

        Parameters
        ----------
        ladder: Ladder
            Ladder object
        Returns
        -------
        bool
        """
        if ladder.top == ladder.bottom:
            raise BoardException(f'A ladder bottom and top cannot be at the same location - {ladder.bottom}')
        if (1 > ladder.top or ladder.top > self.win_position or
                1 > ladder.bottom or ladder.bottom > self.win_position):
            raise BoardException(f'A ladder can be placed within the board between 1 and {self.win_position}')
        if ladder.bottom > ladder.top:
            raise BoardException(f"A ladder's top should always be up from it's bottom")
        if ladder.bottom in self.ladders:
            raise BoardException(f'A ladder bottom already present at the specified bottom location - {ladder.bottom}')
        if ladder.bottom in self.snakes:
            raise BoardException(f'A snake mouth already exists at the specified bottom location - {ladder.bottom}')
        if ladder.bottom in [ladder.top for ladder in self.ladders.values()]:
            raise BoardException(f'A ladder top already present at the specified bottom location - {ladder.bottom}')
        if ladder.bottom in [snake.tail for snake in self.snakes.values()]:
            raise BoardException(f'A snake tail already exists at the specified bottom location - {ladder.bottom}')
        if ladder.top in self.ladders:
            raise BoardException(f'A ladder bottom already present at the specified top location - {ladder.top}')
        if ladder.top in self.snakes:
            raise BoardException(f'A snake mouth already exists at the specified top location - {ladder.top}')
        return True

    def __is_valid_snake(self, snake):
        """
        Validates a given snake.

        Parameters
        ----------
        snake: Snake
            Snake object
        Returns
        -------
        bool
        """
        if snake.mouth == snake.tail:
            raise BoardException(f'A snake mouth and tail cannot be at the same location - {snake.mouth}')
        if (1 > snake.mouth or snake.mouth > self.win_position or
                1 > snake.tail or snake.tail > self.win_position):
            raise BoardException(f'A snake can be placed within the board between 1 and {self.win_position}')
        if snake.tail > snake.mouth:
            raise BoardException(f"A snake's mouth should always be up from it's tail")
        if snake.mouth == self.win_position:
            raise BoardException(f"A snake mouth can't be present at the winning position")
        if snake.mouth in self.ladders:
            raise BoardException(f'A ladder bottom already exists at the specified mouth location - {snake.mouth}')
        if snake.mouth in self.snakes:
            raise BoardException(f'A snake mouth already exists at the specified mouth location - {snake.mouth}')
        if snake.mouth in [ladder.top for ladder in self.ladders.values()]:
            raise BoardException(f'A ladder top already exists at the specified mouth location - {snake.mouth}')
        if snake.mouth in [snake.tail for snake in self.snakes.values()]:
            raise BoardException(f'A snake tail already exists at the specified mouth location - {snake.mouth}')
        if snake.tail in self.ladders:
            raise BoardException(f'A ladder bottom already exists at the specified tail location - {snake.tail}')
        if snake.tail in self.snakes:
            raise BoardException(f'A snake mouth already exists at the specified tail location - {snake.tail}')
        return True

    def default_setup(self):
        """
        Sets a board with default configurations
        """
        print(f'>>>> Loading with default board configurations - {self.rows} rows and {self.columns} columns')
        for bottom, top in DEFAULT_BOARD['ladders']:
            self.add_ladder(bottom, top)

        for mouth, tail in DEFAULT_BOARD['snakes']:
            self.add_snake(mouth, tail)
        print('>>>> Board setup completed')
        print(f'>>>> Reach {self.win_position} on the board to win the game')

    def manual_setup(self):
        """
        Prompts user to set a board with custom configurations
        """
        print(f'>>>> Manually configuring the board with {self.rows} rows and {self.columns} columns')
        if self.win_position == 1:
            print('>>>> Since there is only one block on the board, skipping the snakes and ladders configuration')
            return
        num_of_ladders = enter_a_valid_number('\tQ. How many ladders do you want on board? ')
        if num_of_ladders > 0:
            print('\tFor ladders, bottom and top positions will be provided as comma separated, e.g. 2,98')
            i = 0
            while i < num_of_ladders:
                try:
                    bottom, top = map(lambda num: int(num.strip()),
                                      input(f'\tQ. Enter bottom and top for ladder {i+1}: ').split(','))
                    self.add_ladder(bottom, top)
                    i += 1
                except BoardException as e:
                    print(f'\t>>>> {e.message}')
                except Exception:
                    print(f'\t>>>> Provide correct inputs for ladder {i+1}')

        num_of_snakes = enter_a_valid_number('\tQ. How many snakes do you want on board? ')
        print('\tFor snakes, mouth and tail positions will be provided as comma separated, e.g. 98,2')
        if num_of_snakes > 0:
            i = 0
            while i < num_of_snakes:
                try:
                    mouth, tail = map(lambda num: int(num.strip()),
                                      input(f'\tQ. Enter mouth and tail for snake {i + 1}: ').split(','))
                    self.add_snake(mouth, tail)
                    i += 1
                except BoardException as e:
                    print(f'\t>>>> {e.message}')
                except Exception:
                    print(f'\t>>>> Provide correct inputs for snake {i + 1}')
        print('>>>> Board setup completed')
        print(f'>>>> Reach {self.win_position} on the board to win the game')

    def move_player(self, player, dice_roll):
        """
        Moves a player on the board based on the rolled dice.

        Parameters
        ----------
        player: int
            Player id
        dice_roll: int
            Number got on rolling the dice

        Returns
        -------
        bool
        """
        self.player_dice_rolls[f'Player {player}'] = append(self.player_dice_rolls[f'Player {player}'], int(dice_roll))
        current_position = self.player_positions[f'Player {player}'][-1]
        print(f'>>>> Player {player} is currently at {current_position} on the board')
        updated_position = current_position + dice_roll
        if updated_position > self.win_position:
            print(f'>>>> This dice roll is moving the Player {player} out of the board, try again')
            return False
        print(f'>>>> Moving Player {player} from {current_position} to new position: {updated_position} on the board')
        if updated_position in self.ladders:
            new_position = self.ladders[updated_position].top
            print(f'>>>> WOW! Found a ladder at the new position {updated_position}, '
                  f'jumping to {new_position} on the board')
        elif updated_position in self.snakes:
            new_position = self.snakes[updated_position].tail
            print(f'>>>> OUCH! Found a snake at the new position {updated_position}, '
                  f'falling to {new_position} on the board')
        else:
            new_position = updated_position
        self.player_positions[f'Player {player}'] = append(self.player_positions[f'Player {player}'], new_position)
        return True

    def check_for_victory(self, player):
        """
        Checks whether the player has reached at the win position or not.

        Parameters
        ----------
        player: int
            Player id

        Returns
        -------
        bool
        """
        if self.player_positions[f'Player {player}'][-1] == self.win_position:
            print(f'>>>> HURRAYYYYY! Player {player} won the game')
            return True
        return False

    def save_the_play(self):
        """
        Saves the current game play as a json file.
        """
        game_data = {}
        moves_df = DataFrame()
        rolls_df = DataFrame()
        for player, positions in self.player_positions.items():
            moves_df = concat([moves_df, DataFrame(data={player: positions.astype(int)})], axis=1)
        for player, data in self.player_dice_rolls.items():
            rolls_df = concat([rolls_df, DataFrame(data={player: data.astype(int)})], axis=1)
        game_data['moves'] = moves_df.to_json(orient='records')
        game_data['rolls'] = rolls_df.to_json(orient='records')
        with open(GAME_DATA_FILE, 'w') as file:
            dump(game_data, file)
