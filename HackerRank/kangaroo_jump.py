#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    retVal = 'NO'
    #The case of same speed
    if v1 == v2 and x1 == x2:
        retVal =  'YES'
    elif v1 == v2:
        retVal =  'NO'
     
    x = (x2-x1) / (v1-v2)    
    if (x == round(x) and x > 0):
        retVal= 'YES'
    else:
        retVal= 'NO'

    # The looping way
    """
    for i in range(10000):
        starVal1 = x1  + (v1 * (i))
        starVal2 = x2 +  (v2 * (i))
        print('{0}, {1}, {2}, {3}'.format(starVal1, starVal2, (v1 * (i)), (v2 * (i))))
        if starVal1 == starVal2 :
            strVal = 'YES'
            break
    """
    
    return retVal

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)


