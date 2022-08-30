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
        # Variable global
        self.underlines: str = ''
        # Imprimir la horca
        print(gallow[0])
        self.word = self.get_random_word()


    def get_random_word(self) -> str:
        # Method Obtener una palabra de forma aleatoria
        random_word = random.choice(self.listOfWords)

        # Retornar la palabra en mayúsculas
        return random_word.upper()

    
    def turn_word_in_underlines(self) -> str:
        # Metodo para generar la cadena de underlines (_) para imprimir en pantalla
        # self.underlines = '_ ' * len(self.word)

        print(self.word)
        # return self.underlines
        return '_ ' * len(self.word)

    
    def compare_letters(self, underlines, letter_selected):
        # Metodo para comparar la letra seleccionada con las letras de la palabra
        # underlines_list = []
        # for underline in underlines:
        #     underlines_list.append(underline)
        # Aplicando list comprehensions
        underlines_list = [underline for underline in self.underlines if underline != ' ']

        for letter in self.word:
            if letter_selected == letter:
                self.underlines = f'{self.underlines}{letter} '
            else:
                self.underlines = f'{self.underlines}_ '
        
        print(underlines_list)
        print(self.underlines)



    

def run():
    play = Game()
    ul = play.turn_word_in_underlines()
    print(ul)
    lett = input('Letra: ')
    play.compare_letters('', lett.upper())
    lett = input('Letra: ')
    play.compare_letters('', lett.upper())

if __name__ == '__main__':
    run()