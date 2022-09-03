"""
Class to work with txt files

return an array with the words into the text file
"""

class Files():

    def __init__(self, path_file):
        self.path_file = path_file


    def read(self):
        content_file = []

        with open(self.path_file, "r", encoding="utf-8") as f:
            for line in f:
                # .rstrip('\n') remove carriage return or line feed
                content_file.append(line.rstrip('\n'))
            
        return content_file


    def write(self, arr):
        with open(self.path_file, "w", encoding="utf-8") as f:
            for element in arr:
                f.write(element)
                f.write("\n")


    def write_in_new_line(self, arr):
        with open(self.path_file, "a", encoding="utf-8") as f:
            for element in arr:
                f.write(element)
                f.write("\n")