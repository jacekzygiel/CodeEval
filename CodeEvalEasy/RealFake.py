import sys


def main(input_file):
    with open(input_file, 'r') as lines:
        for line in lines:
            cardNumber = []
            oddDigits = []
            evenDigits = []
            controlSum = 0

            line = line.rstrip('\n').split(' ')
            for element in line:
                for digit in element:
                    cardNumber.append(int(digit))
            revCardNumber = cardNumber[::-1]
            oddDigits = revCardNumber[0:][::2]
            evenDigits = revCardNumber[1:][::2]

            for x in range(0, len(evenDigits)):
                evenDigits[x] = evenDigits[x]*2

            for odd in oddDigits:
                controlSum += odd

            for even in evenDigits:
                controlSum += even

            if controlSum % 10 == 0:
                print 'Real'
            else:
                print 'Fake'


if __name__ == '__main__':
    try:
        main('RealFake.txt')
    except IOError:
        main(sys.argv[1])
