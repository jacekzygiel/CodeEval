import sys


def cleanUp(line):
    line = line.rstrip('\n').split(' ')
    output = ''
    noAlphaFlag = 1
    for item in line:
        for char in item:
            if char.isalpha():
                noAlphaFlag = 0
                output += char.lower()
            else:
                noAlphaFlag += 1

            if noAlphaFlag == 1:
                output += ' '

    if output[-1].isalpha():
        return output
    else:
        return output[:-1]
    # return output[:-1]


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = cleanUp(test)
            print result

if __name__ == '__main__':
    try:
        main('CleanUpTheWords.txt')
    except IOError:
        main(sys.argv[1])
