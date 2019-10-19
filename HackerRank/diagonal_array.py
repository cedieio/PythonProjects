#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    diagonalSum = 0
    diagonalSumReverse = 0
    if arr != None:
        for i in range(len(arr)) :            
            diagonalSum = diagonalSum + arr[i][i]
        for i in range(len(arr)):
            diagonalSumReverse = diagonalSumReverse +  arr[i][(len(arr) - 1) - i]
    return abs( diagonalSum - diagonalSumReverse)



if __name__ == '__main__':
    

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
