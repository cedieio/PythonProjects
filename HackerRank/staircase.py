#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    if n > 0 and n <= 100:
        for x in range(1, n+1):
            arr = [' '] * (n - x)
            arr = arr +  ['#'] * x
            print(''.join(arr))

    
if __name__ == '__main__':
    n = int(input())

    staircase(n)
