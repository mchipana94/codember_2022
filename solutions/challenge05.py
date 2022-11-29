from utils import get_data, evaluate

def round(array:list):
    '''
    get the survivors of a round
    '''
    new_array = list()
    N = len(array)
    if N % 2:
        new_array = array[2:N:2]
    else:
        new_array = array[0:N:2]
    return new_array

def test():
    input = [
        [0,1,2,3,4,5,6,7,8,9],
        [0,2,4,6,8],
        [4,8]
    ]
    output = [
        [0,2,4,6,8],
        [4,8],
        [4]
    ]
    evaluate(round, input, output)

def hunger_games(array:list):
    '''
    return the lat survivor
    '''
    N = len(array)
    idx_array = list(range(0,N))
    while N > 1:
        idx_array = round(idx_array)
        N = len(idx_array)
    return idx_array[0]

def main():
    input_file = './files/mecenas.json'
    data = get_data(input_file, parse=True)
    idx = hunger_games(data)

    print('Result: ',data[idx],'-',idx)

if __name__ == "__main__":
    main()