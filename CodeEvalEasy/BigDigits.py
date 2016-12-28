import sys


def func(line):
    zero = '''-**--
*--*-
*--*-
*--*-
-**--'''
    one = '''--*--
-**--
--*--
--*--
-***-'''
    two = '''***--
---*-
-**--
*----
****-'''
    three = '''***--
---*-
-**--
---*-
***--'''
    four = '''-*---
*--*-
****-
---*-
---*-'''
    five = '''****-
*----
***--
---*-
***--'''
    six = '''-**--
*----
***--
*--*-
-**--'''
    seven = '''****-
---*-
--*--
-*---
-*---'''
    eight = '''-**--
*--*-
-**--
*--*-
-**--'''
    nine = '''-**--
*--*-
-***-
---*-
-**--'''
    vert = '''-
-
-
-
-'''

    alphaToDigit = {0: zero,
                    1: one,
                    2: two,
                    3: three,
                    4: four,
                    5: five,
                    6: six,
                    7: seven,
                    8: eight,
                    9: nine,
                    10: vert}

    #line = line.rstrip().split(';')

    return alphaToDigit[10].join([str(alphaToDigit[int(x)]) if x.isdigit() else '' for x in line.rstrip()])


def main(input_file):
    with open(input_file, 'r') as testCases:

        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('BigDigits.txt')
    except IOError:
        main(sys.argv[1])
