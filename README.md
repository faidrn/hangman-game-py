# HANGMAN GAME

                ##  ##     ###     ###   ## ###### ###     ###     ###     ###   ##   ######     ###     ###     ### ######
                ##  ##    ## ##    ####  ## ##     ####   ####    ## ##    ####  ##   ##        ## ##    ####   #### ##
                ######   #######   ## ## ## ###### ## ## ## ##   #######   ## ## ##   ######   #######   ## ## ## ## ######
                ##  ##  ##     ##  ##  #### ##  ## ##  ###  ##  ##     ##  ##  ####   ##  ##  ##     ##  ##  ###  ## ##
                ##  ## ##       ## ##   ### ###### ##       ## ##       ## ##   ###   ###### ##       ## ##       ## ######


Hangman is a guessing game about the player tries to guess a word by suggesting letters within a certain number of guesses. Originally a Paper-and-pencil game, this version was made with Python as a beginner project.


### How to play this game

Just in case you don't know, in this game, we have to figure out a secret word by guessing one letter at a time. However, with each error, the man will get one step closer to death! The goal is to successfully guess the word before the man gets hanged.

        ________
        | /    |
        |/     O
        |     /|\
        |      |
        |     / \
        |
    --------


Classes (Underline)

Words list:
In the `files.py`, create **Files class** and its methods as described below.

### Files Class
The Files class has constructor method and it expects a string with the path of the txt file with a list of words as the single parameter.


#### Files class methods
Now, let's move to the Files methods.

- read(self) - a method that returns a list of words from the txt file ***words***.

- write(self, arr) - a method that get a array of new words and to add them at txt files ***words***. To be to be implemented later.

- write_in_new_line(self, arr) - a method that get a array of new words and to add them in a new line into the txt files. To be to be implemented later.



The game logic:
In the `game.py`, create **Game class** and its methods as described below.


### Game Class
This class has constructor method and it expects a string with the game, the words list.

#### Game class methods

+ __init__(self) - method constructor that: 
    + Get the game title and print it 
    + Get the list of words
    + Define global variables 

+ get_random_word(self) - method to get a random word from the words list and return it capitalized.

+ turn_word_in_underlines(self) - method to turn the world in an underlines string (_), to print in screen.

+ compare_letters(self, letter_selected) - method to compare the typed letter with the letters of the word.

+ print_scores(self) - method to print the scores.

+ drawing_hangman(self) - method to print the hangman screen when player typed a wrong letter.

+ game_start(self) - method to clean the board and reset the variables when player start a new game.

+ game_over(self) - method to ask the player about to start a new game every time the game is over.

+ clear(self) - method to clean the terminal every time the game start.



# License
Hangman game is open-source project and distributed under [MIT](https://github.com/faidrn/hangman-game-py/blob/main/LICENSE) license