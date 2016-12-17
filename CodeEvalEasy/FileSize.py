import sys
import os


def main(input_file):
    # with open(input_file, 'r') as lines:

    stat = os.stat(input_file)
    print stat.st_size


if __name__ == '__main__':
    try:
        main('BitPositions.txt')
    except:
        main(sys.argv[1])