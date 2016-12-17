'''
Created on Nov 3, 2016

@author: zygielj
'''
import sys


# with open(sys.argv[1], 'r') as lines
with open('AgeDistribution.txt', 'r') as lines:
    for line in lines:
        age = int(line)
        if age >= 0 and age < 3:
            print "Still in Mama's arms"
        elif age >= 3 and age < 5:
            print "Preschool Maniac"
        elif age >= 5 and age < 12:
            print "Elementary school"
        elif age >= 12 and age < 15:
            print "Middle school"
        elif age >= 15 and age < 19:
            print "High school"
        elif age >= 19 and age < 23:
            print "College"
        elif age >= 23 and age < 66:
            print "Working for the man"
        elif age >= 66 and age < 101:
            print "The Golden Years"
        elif age < 0 or age > 100:
            print "This program is for humans"

if __name__ == '__main__':
    pass
