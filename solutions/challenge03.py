from utils import get_data, evaluate

class Zebra:
    def __init__(self, color1=None, color2=None):
        self.is_finished = False
        self.size = 0
        self.index = 0
        self.colors = {0: None, 1: None}
        self.add(color1)
        self.add(color2)
    
    def add(self, color):
        if self.is_finished or color is None:
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

def get_big_zebra(color_array):
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
    input = [
        ['red', 'blue', 'red', 'blue', 'green'],
        ['green', 'red', 'blue', 'gray'],
        ['blue', 'blue', 'blue', 'blue'],
        ['red', 'green', 'red', 'green', 'red', 'green'],
        ['red', 'red', 'blue', 'red', 'red', 'red', 'green'],
        ['green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'green', 'red', 'gray', 'blue']
    ]

    output = [
        (4, 'blue'),
        (2, 'gray'),
        (1, 'blue'),
        (6, 'green'),
        (3, 'red'),
        (6, 'red')
    ]

    evaluate(get_big_zebra, input, output)

def main():
    input_file = './colors.txt'
    data = get_data(input_file, parse=True)

    print('Result: ',get_big_zebra(data))
    
if __name__ == "__main__":
    main()