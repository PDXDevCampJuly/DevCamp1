from sys import argv

def get_secret(fileName):
    with open(fileName, "r") as f:
        output = f.read()
    return output
    #f = open(fileName, "r")
    #f.read(string)
    #f.close()


def detransform(string):
    charList = string.split()
    message = ""
    for char in charList:
        if len(char) >= 7:
            #message += chr()
            pass
        else:
            message += chr(int(char))
    return message

def main():
    if len(argv) > 2:
        print("""Usage: decode.py <fileName>""")
    else:
        try:
            fileName = argv[1]
        except IndexError:
            fileName = 'secret.txt'
        secret = get_secret(fileName)
        decodedMessage = detransform(secret)
        print(decodedMessage)

if __name__ == '__main__':
    main()
