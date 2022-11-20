from utils import get_data, evaluate

def decode_word(word):
    output = ''
    i = 0
    while i < len(word):
        if word[i] == '1':
            output += chr(int(word[i:i+3]))
            i += 3
        else:
            output += chr(int(word[i:i+2]))
            i += 2
    return output
               
def decode_message(message):
    words = message.split()
    output = list()
    for word in words:
        output.append(decode_word(word))
    return ' '.join(output)

def encode_mesage(message):
    output = ''
    for character in message:
        if character == ' ':
            output += ' '
        else:
            output += str(ord(character))
    return output

def test():
    input = ["109105100117", "9911110010110998101114", "9911110010110998101114 109105100117", "11210897121 116101116114105115"]
    output = ["midu", "codember", "codember midu", "play tetris"]

    evaluate(decode_message, input, output)
    
def main():
    input_file = './files/encrypted.txt'
    message = get_data(input_file)

    print('Encoded Message: ',message)
    print('Decoded Message: ',decode_message(message))

if __name__ == "__main__":
    main()