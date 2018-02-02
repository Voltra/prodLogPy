#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Array import Array

def generalSum(lhs, rhs):
    return lhs + rhs
#

if __name__ == "__main__":
    with open("../rsc/test_val", "r") as fic:
        line = fic.readline()
        arr = Array(line.split(" "))
        processedSum = arr.map(int).reduce(generalSum)
        joined = arr.join("+")
        print("%s = %s" % (joined, processedSum))
    #

        '''
        arr.map(int).filter(isNotZero).reduce(makeSum)
        
        VS
        
        reduce(makeSum, filter(isNotZero, map(int, arr)))
        
        or
        
        reduce(
            makeSum,
            filter(
                isNotZero,
                map(int, arr)
            )
        )
        '''
#