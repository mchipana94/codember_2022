from utils import evaluate

def eval_number(number):
    digits = list(map(int, f"{number}"))
    digit_ant = digits[0]
    five_cont = 1 if digit_ant == 5 else 0
    for digit in digits[1:]:
        if digit < digit_ant:
            return False
        if digit == 5 :
            five_cont += 1
        digit_ant = digit
    if five_cont >= 2:
        return True
    else:
        return False

def generate_numbers(start, end):
    valid_numbers = []
    for i in range(start, end):
        if eval_number(i):
            valid_numbers.append(i)
    return valid_numbers

def test():
    input = [55678, 12555, 55555, 12345, 57775]
    output = [True, True, True, False, False]
    evaluate(eval_number, input, output)

def main():
    numbers = generate_numbers(11098, 98123)
    print('Result: %d-%d'%(len(numbers), numbers[54]))


if __name__ == "__main__":
    main()