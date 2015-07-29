from sys import argv


def transform(string):
    output = []
    for char in string:
        output.append(str(ord(char)))
    return ' '.join(output)


def make_secret(string, fileName):
    f = open(fileName, "w")
    f.write(string)
    f.close()
    #with open(fileName, 'w') as f:
    #    f.write(string)


def main ():
    if len(argv) > 3:
        print(
            """Usage: encode.py <message> <filename>"""
        )
    else:
        try:
            fileName = argv[2]
        except IndexError:
            fileName = 'secret.txt'
        try:
            message = argv[1]
        except IndexError:
            message = input("What message would you like to send? >> ")
        encodedMessage = transform(message)

        make_secret(encodedMessage, fileName)


if __name__ == '__main__':
    main()
