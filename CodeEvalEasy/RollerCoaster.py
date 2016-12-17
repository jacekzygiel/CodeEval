import sys


def main(input_file):
    with open(input_file, 'r') as lines:
        for line in lines:
            numberOfChar = 0
            output = ''
            for element in line:
                if element.isalpha():
                    if numberOfChar % 2 == 0:
                        output += element.upper()
                    else:
                        output += element.lower()
                    numberOfChar += 1
                else:
                    output += element
            print output


if __name__ == '__main__':
    try:
        main('RollerCoaster.txt')
    except IOError:
        main(sys.argv[1])
