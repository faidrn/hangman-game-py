"""
Class with the logic game

"""

from title_game import title_game as tg
from screens_hangman import screens_dict as gallow
from files import Files
import random

class Game():

    # Method constructor
    def __init__(self):
        self.title = tg()
        print(self.title)
        # Leer el archivo txt
        file = Files('./words.txt')
        # Obtener la lista de palabras
        self.listOfWords = file.read()
        # Imprimir la horca
        print(gallow[0])
        self.word = self.get_random_word()


    def get_random_word(self) -> str:
        # Obtener una palabra de forma aleatoria
        random_word = random.choice(self.listOfWords)

        # Retornar la palabra en mayúsculas
        return random_word.upper()

    
    def turn_word_in_underlines(self):
        underlines = '_ ' * len(self.word)

        print(underlines)
    

def run():
    play = Game()
    play.turn_word_in_underlines()

if __name__ == '__main__':
    run()