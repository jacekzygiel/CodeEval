'''
Created on Nov 2, 2016

@author: zygielj
'''
import sys
import string


def lowerCaseDict(shift):
    lowerCase = string.ascii_lowercase
    beautyLevel = {}
    val = []
    for x in range(0, 26):
        val.append(x+1)

    shifted = val[shift:] + val[:shift]
    for x in range(0, 26):
        beautyLevel[lowerCase[x]] = shifted[x]
    return beautyLevel


def letterValue(dictionary, letter):
    letter = letter.lower()
    try:
        val = dictionary[letter]
    except KeyError:
        return 0
    return val


def checkValue(input):
    with open('input, 'r') as strings:
        for line in strings:
            lineVal = 0
            maxLineVal = 0
            for shift in range(26):
                dictionary = lowerCaseDict(shift)
                lineVal = 0
                for letter in line:
                    letVal = letterValue(dictionary, letter)
                    lineVal += letVal
                if maxLineVal < lineVal:
                    maxLineVal = lineVal
                    print shift
            print maxLineVal

if __name__ == '__main__':
    try:
        checkValue('MixedContent.txt')
    except IOError:
        checkValue(sys.argv[1])


