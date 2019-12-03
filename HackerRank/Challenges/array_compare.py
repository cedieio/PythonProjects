#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    retValue = []
    aValue = 0
    bValue = 0
    if len(a) == 3 and len(b) == 3:
        for i in range(3):
            if a[0] > 0 and a[0] <= 100 and b[0] > 0 and b[0] <= 100:
                if a[i] > b[i]:
                    aValue = aValue+1
                elif a[i] < b[i]:
                    bValue = bValue+1                
    retValue.append( aValue )
    retValue.append( bValue )
    return retValue
if __name__ == '__main__':
    

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
