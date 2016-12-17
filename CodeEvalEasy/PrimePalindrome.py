'''
Created on Nov 3, 2016

@author: zygielj
Topic:
Write a program which determines the largest prime palindrome less than 1000. 
'''


def palindrome():
    for x in range(1000, -1, -1):
        if str(x) == (str(x)[::-1]):
            if prime(x) == True:
                return x
            else:
                pass
        else:
            pass


def prime(number):
    y = 2
    if number < 2:
        return False
    while y < number:
        if number % y == 0:
            return False
        y += 1
    return True

if __name__ == '__main__':
    print palindrome()
