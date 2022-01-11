# nagp_snakes_and_ladders
A console based snakes and ladders game built in Python.

First steps
-
#### Prerequisite
- Python 3.7.x

#### Installation
1. Create a virtual environment
    ```shell script
    python -m venv venv
    ```

2. Activate the environment
    ```
    venv\Scripts\activate
    ```

3. Install the requirements
    ```
    pip install -r requirements.txt
    ```
 
#### Start the Game
Run below command to start the game on console
```
    python app.py
```

Rules
-
1. Board
    1. Default board configurations 
        - Rows - 10
        - Columns - 10
        - for snakes and ladders position, refer to [constants](https://github.com/himanshusb12/nagp_snakes_and_ladders/blob/master/shared/constants.py#L3).
    2. Manual board configuration
        - Rows - as per choice, a valid non zero positive integer. It's recommended to have a value greater than 5 to play a proper game.
        - Columns - as per choice, a valid non zero positive integer. It's recommended to have a value greater than 5 to play a proper game.
        - Snakes
            1. Number of snakes - as per choice
            2. Location of a snake - provide a snake position by providing it's mouth and tail location in the console. Format - mouth, tail
            3. Rules to keep in mind while placing a snake on the board
                - A snake mouth and tail cannot be at the same location
                - A snake can be placed within the board only
                - A snake's mouth should always be up from it's tail
                - A snake mouth cannot be present at the winning position
                - A ladder bottom should not exist at the specified mouth location
                - Another snake mouth should not exist at the specified mouth location
                - A ladder top should not exist at the specified mouth location
                - Another snake tail should not exist at the specified mouth location
                - A ladder bottom should not exist at the specified tail location
                - Another snake mouth already exist at the specified tail location
        - Ladders
            1. Number of ladders - as per choice
            2. Location of a ladder - provide a ladder position by providing it's bottom and top location in the console. Format - bottom, top
            3. Rules to keep in mind while placing a ladder on the board
                - A ladder bottom and top cannot be at the same location
                - A ladder can be placed within the board only
                - A ladder's top should always be up from it's bottom
                - Another ladder bottom cannot be present at the specified bottom location
                - A snake mouth should not exist at the specified bottom location
                - Another ladder top should not exist at the specified bottom location
                - A snake tail should not exist at the specified bottom location
                - Another ladder bottom should not exist at the specified top location
                - A snake mouth should not exist at the specified top location
    3. Winning criteria
        - Any player how reaches to the last position on the board (number of row x number of column) wins the game.
                   
2. Dice
    1. Default dice configurations 
        - Minimum number - 1
        - Maximum number - 6
    2. Manual dice configuration
        - Minimum number - as per choice, a valid non zero positive integer.
        - Maximum number - as per choice, a valid non zero positive integer.
    3. Re-roll criteria
        - If a player gets the maximum number on the dice, one more dice roll is awarded to the player.
        
3. How to Play?
    1. Requires at-least 2 players to start a game.  
    2. Either laod default configuration automatically or set custom configurations manually for a game board and dice.
    3. On each player's turn, hit enter to roll a dice and follow the instructions on the console.
    
4. Statistical Analysis
    1. Application allows the user to load and analyze last played game's data.
    2. The game data is stored in [last_game.json](https://github.com/himanshusb12/nagp_snakes_and_ladders/blob/master/data/last_game.json).
    3. After every game, this json file is overwritten with the latest game play.
    4. Either choose a line plot to see all players progress through out the game or choose a count plot to see how many times a dice number was rolled by each player.
    5. You can also see the data directly as individual dataframes on the console.