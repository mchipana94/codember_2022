import ast

def get_data(filename, parse=False):
    archive = open(filename, 'r')
    data = archive.read()
    archive.close()
    if parse:
        return ast.literal_eval(data)
    return data

def evaluate(function, inputs, outputs):
    N = min(len(inputs),len(outputs))
    for i in range(N):
        result = function(inputs[i]) == outputs[i]
        print('* Test #{}: '.format(i+1), 'Passed' if result else 'Wrong')