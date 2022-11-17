input_file = './encrypted.txt'

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

def main():
    archive = open(input_file, 'r')
    message = archive.read()
    archive.close()
    print('Encoded Message: ',message)
    print('Decoded Message: ',decode_message(message))

main()