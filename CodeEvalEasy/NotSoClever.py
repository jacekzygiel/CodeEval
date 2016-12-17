import sys


def stupid_sort(array, iterations):
    for i in range(iterations):
        for j in range(len(array)-1):
            if int(array[j]) > int(array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                break
    return array


def main(input):
    with open(input, 'r') as lines:
        for line in lines:
            sort = []
            numOfIter = []
            toPrint = ''
            sort, numOfIter = line.split('|')
            sort = sort.split()
            numOfIter = int(numOfIter)
            sort = stupid_sort(sort, numOfIter)
            print(' '.join(s for s in sort))

if __name__ == '__main__':
    try:
        main('NotSoClever.txt')
    except IOError:
        main(sys.argv[1])
