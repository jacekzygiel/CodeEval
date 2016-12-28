import sys


def func(line):
    right = {'(': ')',
             '[': ']',
             '{': '}'}
    left = {')': '(',
            ']': '[',
            '}': '{'}

    rightOrd = []
    leftOrd = []

    leftS = [')', ']', '}']
    rightS = ['(', '[', '{']

    for element in line:
        if element in rightS[::2]:
            rightOrd.append(element)
        elif element in leftS:
            leftOrd.append(element)

    leftOrd = leftOrd[::-1]

    if len(leftOrd) != len(rightOrd):
        return False
    else:
        for x in range(len(rightOrd)):
            if rightOrd[x] != (left[leftOrd[x]]):
                return False
        return True


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('ValidParentheses.txt')
    except IOError:
        main(sys.argv[1])
