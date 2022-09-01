"""
Hangman game by Fredy Izquierdo

Class to play the game

Github: https://github.com/faidrn
Twitter: https://twitter.com/_FAID__
Website: https://faidrn.github.io/hello-world/
"""

from game import Game


def run():
    play_game = Game()

    # Start the first game
    play: str = 's'

    while play != 'n':
        continue_loop = True
        play_game.game_start()

        while continue_loop:
            letter_selected = input('Letra: ')
            continue_loop = play_game.compare_letters(letter_selected.upper())

        play = play_game.game_over()


if __name__ == '__main__':
    run()
