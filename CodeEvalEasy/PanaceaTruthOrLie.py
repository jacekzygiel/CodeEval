'''
Created on Nov 3, 2016

@author: zygielj
'''
import sys


# with open(sys.argv[1], 'r') as lines:
with open('PanaceaTruthOrLie.txt', 'r') as lines:
    for line in lines:
        virus = []
        antyvirus = []
        virusVal = 0
        antyVal = 0

        virus, antyvirus = line.split("|")
        virus = virus.split()
        antyvirus = antyvirus.split()

        for x in virus:
            x = int(x, 16)
            virusVal += x
        print virusVal

        for y in antyvirus:
            y = int(y, 2)
            antyVal += y
        print antyVal

        if virusVal <= antyVal:
            print True
        else:
            print False

if __name__ == '__main__':
    pass
