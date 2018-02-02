#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xPlusY import parseInt

'''
Determines whether or not a number is a prime number
@param n being the number to test
@returns TRUE if prime FALSE otherwise
'''
def isPrime(n):
    if n <= 0:
        raise AssertionError("Can't determine if a number is prime if the said number is <= 0")

    if n == 1:
        return False

    for number in range(2, n):
        if n%number == 0 and n!=number:
            return False
        '''
        If there's a number N in [2, n) that is != n then it is not a prime number
        Since prime numbers are numbers that can only be divided by 1 and themselves
        '''

    return True

if __name__ == "__main__":
    userInput = parseInt(input("number: "))
    print("is prime" if isPrime(userInput) else "is not prime")