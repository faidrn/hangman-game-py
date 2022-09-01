"""
Class with the logic game

"""

from operator import truediv
from title_game import title_game as tg
from screens_hangman import screens_dict as gallow
from files import Files
import random
# Framework to use terminal functions
import os
from time import sleep


class Game():

    # Method constructor
    def __init__(self):
        self.title = tg()
        print(self.title)
        # Read the txt file
        file = Files('./words.txt')
        # file = Files('/Users/macbook/Documents/Projects/python/hangman-game-py/words.txt')
        # Get the list of words
        self.listOfWords = file.read()
        # Variable to know if player guess the letter
        self.guessTheLetter: bool = False
        # Variables to show the scores
        self.wrongScore: int = 0
        self.successScore: int = 0
        # Number of bad answers
        self.numberOfBadAnswers: int = 0
        # Number of success answers
        self.numberOfCorrectAnswers: int = 0
        # Position the screen into the screens_dict 
        self.screenNumber = 1
        

    def get_random_word(self) -> str:
        # Method Obtener una palabra de forma aleatoria
        random_word = random.choice(self.listOfWords)

        # Return the capitalized word
        return random_word.upper()

    
    def turn_word_in_underlines(self) -> str:
        # Method to get the underlines string (_) to print in screen
        # Apply list comprehensions
        self.underlines = ['_' for i in range(len(self.word))]

        print(" ".join(self.underlines))
        return self.underlines

    
    def compare_letters(self, letter_selected) -> bool:
        # Method to compare the selected letter with the letters of the word
        # Variable to keep the loop to type the letters
        continue_loop = True

        for i in range(len(self.word)):
            if letter_selected == self.word[i]:
                self.underlines[i] = letter_selected
                self.guessTheLetter = True
                self.numberOfCorrectAnswers += 1
        
        print(" ".join(self.underlines))

        if self.guessTheLetter == False:
            self.drawing_hangman()
            self.numberOfBadAnswers += 1

        self.guessTheLetter = False

        # Show messages if player win or not
        # 6 screens of the hangman
        if self.numberOfBadAnswers == 6:
            print(f'Perdiste!. La palabra era {self.word}')

            self.wrongScore += 1
            continue_loop = False
            self.print_scores()
        else:
            # Message if player win
            if self.numberOfCorrectAnswers == len(self.word):
                print(f'Felicidades! Has adivinado la palabra')
                self.successScore += 1
                continue_loop = False
                self.print_scores()


        return continue_loop


    def print_scores(self):
        # Method to print the scores
        print(f'Aciertos: {self.successScore}')
        print(f'Desaciertos: {self.wrongScore}')


    def drawing_hangman(self):
        # Method to print the hangman screen
        print(gallow[self.screenNumber])
        self.screenNumber += 1


    def game_start(self):
        # Method to clean the board and reset the variables

        # Wait 2 seconds to clean the screen
        sleep(2)
        # Clear the terminal
        self.clear()

        # Reset variables
        self.screenNumber = 1
        self.numberOfBadAnswers = 0
        self.numberOfCorrectAnswers = 0

        print(gallow[0])
        self.word = self.get_random_word()
        self.underlines = self.turn_word_in_underlines()


    def game_over(self):
        # Method to ask about a new game
        play_again = input('Continuar jugando [s/n]: ')

        return play_again



    def clear(self):
        # Method to clean the terminal
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)



    

# def run():
#     play = Game()
#     ul = play.turn_word_in_underlines()
#     print(" ".join(ul))
#     lett = input('Letra: ')
#     play.compare_letters(lett.upper())
#     lett = input('Letra: ')
#     play.compare_letters(lett.upper())
#     lett = input('Letra: ')
#     play.compare_letters(lett.upper())
#     lett = input('Letra: ')
#     play.compare_letters(lett.upper())
#     lett = input('Letra: ')
#     play.compare_letters(lett.upper())
#     lett = input('Letra: ')
#     play.compare_letters(lett.upper())
#     lett = input('Letra: ')
#     play.compare_letters(lett.upper())
#     lett = input('Letra: ')
#     play.compare_letters(lett.upper())

# if __name__ == '__main__':
#     run()