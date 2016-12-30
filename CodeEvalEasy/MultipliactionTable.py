import sys
import os


def main():
    tabFinal=[]
    for x in range(1, 13):
        tabTemp = []
        for y in range(1, 13):
            tabTemp.append(x*y)
        tabFinal.append(tabTemp)
    print '\n'.join(str(''.join('{:>4}'.format(str(x)) for x in tabFinal[y])) for y in range(len(tabFinal)))

if __name__ == '__main__':
    main()
