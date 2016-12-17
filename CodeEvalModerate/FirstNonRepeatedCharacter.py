import sys


def func(line):
    for x in range(len(line)):
        let = line[x]
        pre = line[:x]
        post = line[x+1:]

        if pre.find(let) == -1 and post.find(let) == -1:
            return let
    return


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('FirstNonRepeatedCharacter.txt')
    except IOError:
        main(sys.argv[1])
