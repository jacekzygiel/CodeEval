'''
Created on Nov 3, 2016

@author: zygielj
'''
import sys
import re


def main():
    # with open(sys.argv[1], 'r') as lines:
    with open('EmailValidation.txt', 'r') as lines:
        EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        for line in lines:
            if EMAIL_REGEX.match(line):
                print 'true'
            else:
                print 'false'

if __name__ == '__main__':
    main()
