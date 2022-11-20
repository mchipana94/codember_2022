import ast

input_file = './colors.txt'

class Zebra:
    def __init__(self, color1=None, color2=None):
        self.is_finished = False
        self.size = 0
        self.index = 0
        self.colors = {0: None, 1: None}
        self.add(color1)
        self.add(color2)
    
    def add(self, color):
        if color is None:
            return None
        if self.is_finished:
            return None
        if self.size == 0:
            self.colors[0] = color
            self.size += 1
        elif self.size == 1:
            if not color == self.colors[0]:
                    self.colors[1] = color
                    self.size +=1
                    self.index = 1 
        else:
            if color == self.colors[not self.index]:
                self.size += 1
                self.index = (self.size - 1) % 2
            else:
                self.is_finished = True
                
    def get_last(self):
        return self.colors[self.index]
    
    def __eq__(self, other):
        return self.size == other.size

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __le__(self, other):
        return self.size <= other.size

    def __ge__(self, other):
        return self.size >= other.size

def eval_serie(color_array):
    zebras = [Zebra()]
    for color in color_array:
        zebra = zebras[-1]
        zebra.add(color)
        if zebra.is_finished:
            zebra2 = Zebra(zebra.get_last(), color)
            zebras.append(zebra2)
    
    zebra_max = Zebra()
    for zebra in zebras:
        if zebra >= zebra_max:
            zebra_max = zebra
    return zebra_max.size, zebra_max.get_last()

def test():
    examples = [
        (['red', 'blue', 'red', 'blue', 'green'],(4, 'blue')),
        (['green', 'red', 'blue', 'gray'],(2, 'gray')),
        (['blue', 'blue', 'blue', 'blue'],(1, 'blue')),
        (['red', 'green', 'red', 'green', 'red', 'green'],(6, 'green')),
        (['red', 'red', 'blue', 'red', 'red', 'red', 'green'],(3, 'red')),
        (['green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'red', 'gray', 'blue'],(6, 'red'))
    ]

    for example,result in examples:
        output = eval_serie(example)
        print( 'Passed' if output==result else 'Wrong')

def main():
    archive = open(input_file, 'r')
    message = archive.read()
    archive.close()
    lista = ast.literal_eval(message.replace('\n', ''))
    print('Result: ',eval_serie(lista))
    
main()