from .ladder import Ladder
from .snake import Snake
from shared.exception import BoardException
from shared.utils import enter_a_valid_number


DEFAULT_BOARD = {
    'snakes': [(99, 2), (90, 76), (81, 33), (73, 56), (65, 11), (61, 40), (51, 27), (47, 17), (32, 10), (26, 17),
               (20, 4), (19, 8)],
    'ladders': [(5, 34), (14, 98), (12, 21), (22, 75), (28, 41), (35, 45), (39, 89), (42, 67), (53, 69), (60, 88),
                (66, 93), (78, 91)]
}


class Board:
    def __init__(self, num_of_players, rows=10, columns=10):
        self.rows = rows
        self.columns = columns
        self.ladders = {}
        self.snakes = {}
        self.player_positions = {player: 0 for player in range(1, num_of_players + 1)}

    def add_ladder(self, bottom, top):
        ladder = Ladder(bottom=bottom, top=top)
        if self.__is_valid_ladder(ladder):
            self.ladders[bottom] = ladder

    def add_snake(self, mouth, tail):
        snake = Snake(mouth=mouth, tail=tail)
        if self.__is_valid_snake(snake):
            self.snakes[mouth] = snake

    def __is_valid_ladder(self, ladder):
        if (1 > ladder.top or ladder.top > self.rows * self.columns or
                1 > ladder.bottom or ladder.bottom > self.rows * self.columns):
            raise BoardException(f'A ladder can be placed within the board between 1 and {self.rows * self.columns}')
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
        # if ladder.top in [ladder.top for ladder in self.ladders.values()]:
        #     raise BoardException(f'A ladder top already present at the specified top location - {ladder.top}')
        # if ladder.top in [snake.tail for snake in self.snakes.values()]:
        #     raise BoardException(f'A snake tail already exists at the specified top location - {ladder.top}')
        return True

    def __is_valid_snake(self, snake):
        if (1 > snake.mouth or snake.mouth > self.rows * self.columns or
                1 > snake.tail or snake.tail > self.rows * self.columns):
            raise BoardException(f'A snake can be placed within the board between 1 and {self.rows * self.columns}')
        if snake.mouth in self.ladders:
            raise BoardException(f'A ladder bottom already exist at the specified mouth location - {snake.mouth}')
        if snake.mouth in self.snakes:
            raise BoardException(f'A snake mouth already exist at the specified mouth location - {snake.mouth}')
        if snake.mouth in [ladder.top for ladder in self.ladders.values()]:
            raise BoardException(f'A ladder top already exist at the specified mouth location - {snake.mouth}')
        if snake.mouth in [snake.tail for snake in self.snakes.values()]:
            raise BoardException(f'A snake tail already exist at the specified mouth location - {snake.mouth}')
        if snake.tail in self.ladders:
            raise BoardException(f'A ladder already exist at the specified tail location - {snake.tail}')
        if snake.tail in self.snakes:
            raise BoardException(f'A snake already exist at the specified tail location - {snake.tail}')
        # if snake.tail in [ladder.top for ladder in self.ladders.values()]:
        #     raise BoardException(f'A ladder top already exist at the specified tail location - {snake.tail}')
        # if snake.tail in [snake.tail for snake in self.snakes.values()]:
        #     raise BoardException(f'A snake tail already exist at the specified tail location - {snake.tail}')
        return True

    def default_setup(self):
        print('>>>> Loading with default board configurations')
        for bottom, top in DEFAULT_BOARD['ladders']:
            self.add_ladder(bottom, top)

        for mouth, tail in DEFAULT_BOARD['snakes']:
            self.add_snake(mouth, tail)
        print('>>>> Board setup completed')

    def manual_setup(self):
        print(f'>>>> Manually configuring the board with {self.rows} rows and {self.columns} columns')
        num_of_ladders = enter_a_valid_number('\tHow many ladders do you want on board? ')
        print('\tFor ladders, bottom and top positions will be provided as comma separated with no space, e.g. 2,98')
        i = 0
        while i < num_of_ladders:
            try:
                bottom, top = map(lambda num: int(num.strip()),
                                  input(f'\tEnter bottom and top for ladder {i+1}: ').split(','))
                self.add_ladder(bottom, top)
                i += 1
            except BoardException as e:
                print(f'\t>>>> {e.message}')
            except:
                print(f'\t>>>> Provide correct inputs for ladder {i+1}')

        num_of_snakes = enter_a_valid_number('\tHow many snakes do you want on board? ')
        print('\tFor snakes, mouth and tail positions will be provided as comma separated with no space, e.g. 98,2')
        i = 0
        while i < num_of_snakes:
            try:
                mouth, tail = map(lambda num: int(num.strip()),
                                  input(f'\tEnter mouth and tail for snake {i + 1}: ').split(','))
                self.add_snake(mouth, tail)
                i += 1
            except BoardException as e:
                print(f'\t>>>> {e.message}')
            except:
                print(f'\t>>>> Provide correct inputs for snake {i + 1}')
        print('>>>> Board setup completed')

    def move_player(self, player, dice_roll):
        current_position = self.player_positions[player]
        updated_position = current_position + dice_roll
        if updated_position > self.rows * self.columns:
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
        self.player_positions[player] = new_position
        return True

    def check_for_victory(self, player):
        if self.player_positions[player] == self.rows * self.columns:
            print(f'>>>> HURRAYYYYY! Player {player} won the game')
            return True
        return False
