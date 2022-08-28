"""
Class to work with txt files

Hangman game by Fredy Izquierdo

Github: https://github.com/faidrn
Twitter: https://twitter.com/_FAID__
Website: https://faidrn.github.io/hello-world/
"""

class Files():

    def __init__(self, path_file):
        self.path_file = path_file


    def read(self):
        content_file = []

        with open(self.path_file, "r", encoding="utf-8") as f:
            for line in f:
                # .rstrip('\n') elimina el retorno de carro o salto de linea
                content_file.append(line.rstrip('\n'))
            
        return content_file


    def write(self, arr):
        # arr = ["Nicolás", "Miguel", "Pepe", "Christian", "Rocío"]

        with open(self.path_file, "w", encoding="utf-8") as f:
            for element in arr:
                f.write(element)
                f.write("\n")


    def write_in_new_line(self, arr):
        # arr = ["Facundo", "Miguel", "Pepe", "Christian", "Rocío"]
        # arr = ["María", "Fernanda"]

        with open(self.path_file, "a", encoding="utf-8") as f:
            for element in arr:
                f.write(element)
                f.write("\n")


def run():
    file = Files('./words.txt')
    print(file.read())
    # file.write()
    # file.write_in_new_line()


if __name__ == '__main__':
    run()