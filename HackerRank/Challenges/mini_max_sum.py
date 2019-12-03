#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arrMinimum = arr[:]
    arrMaximum = arr[:]
    del arrMinimum[arrMinimum.index(max(arrMinimum))]
    del arrMaximum[arrMaximum.index(min(arrMaximum))]
    print('{0} {1}'.format(sum(arrMinimum), sum(arrMaximum)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
