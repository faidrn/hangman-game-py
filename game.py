"""
Class with the logic game

"""

from title_game import title_game as tg
from screens_hangman import screens_dict as gallow
from files import Files
import random
# Libreria para usar funciones de la consola
import os

class Game():

    # Method constructor
    def __init__(self):
        self.title = tg()
        print(self.title)
        # Leer el archivo txt
        file = Files('./words.txt')
        # file = Files('/Users/macbook/Documents/Projects/python/hangman-game-py/words.txt')
        # Obtener la lista de palabras
        self.listOfWords = file.read()
        # Variable global
        self.underlines = []
        # Imprimir la horca
        print(gallow[0])
        self.word = self.get_random_word()
        # Variable auxiliar para saber si ha adivinado o no una letra
        self.guessTheLetter: bool = False
        # Variables para llevar los puntos a favor y en contra
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

        # Retornar la palabra en mayúsculas
        return random_word.upper()

    
    def turn_word_in_underlines(self) -> str:
        # Metodo para generar la cadena de underlines (_) para imprimir en pantalla
        # Aplicando list comprehensions
        self.underlines = ['_' for i in range(len(self.word))]

        print(self.word)
        return self.underlines
        # return '_ ' * len(self.word)

    
    def compare_letters(self, letter_selected) -> bool:
        # Metodo para comparar la letra seleccionada con las letras de la palabra
        for i in range(len(self.word)):
            if letter_selected == self.word[i]:
                # underlines_list[i] = letter_selected
                self.underlines[i] = letter_selected
                self.guessTheLetter = True
                self.numberOfCorrectAnswers += 1
        
        print(" ".join(self.underlines))

        if self.guessTheLetter == False:
            self.drawing_hangman()
            self.numberOfBadAnswers += 1

        # Mostrar mensaje de perdiste
        # 6 partes del cuerpo
        if self.numberOfBadAnswers == 6:
            # Agregar la palabra al mensaje
            print(f'Perdiste!. La palabra era {self.word}')

            self.wrongScore += 1
        else:
            # Mostrar el mensaje de ganaste
            if self.numberOfCorrectAnswers == len(self.word):
                print(f'Felicidades! Has adivinado la palabra')
                self.successScore += 1

        self.guessTheLetter = False

        return True


    def drawing_hangman(self):
        # Method to print the hangman screen
        print(gallow[self.screenNumber])
        self.screenNumber += 1


    def game_start(self):
        # Method tho reset the board and variables
        # Clear the terminal
        self.clear()

        # Reset variables
        self.screenNumber = 1
        self.numberOfBadAnswers = 0
        self.numberOfCorrectAnswers = 0


    def game_over(self):
        # Method to ask about a new game
        play_again = input('Continuar jugando [s/n]: ')

        if (play_again == 's'):
            self.game_start()
            self.get_random_word()
            # pendiente agregar la forma de que el juego se inicie(equivalente a desbloquear botones)
        else:
            return



    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")



    

def run():
    play = Game()
    ul = play.turn_word_in_underlines()
    print(" ".join(ul))
    lett = input('Letra: ')
    play.compare_letters(lett.upper())
    lett = input('Letra: ')
    play.compare_letters(lett.upper())
    lett = input('Letra: ')
    play.compare_letters(lett.upper())
    lett = input('Letra: ')
    play.compare_letters(lett.upper())
    lett = input('Letra: ')
    play.compare_letters(lett.upper())
    lett = input('Letra: ')
    play.compare_letters(lett.upper())
    lett = input('Letra: ')
    play.compare_letters(lett.upper())
    lett = input('Letra: ')
    play.compare_letters(lett.upper())

if __name__ == '__main__':
    run()