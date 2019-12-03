#!/bin/python3
"""
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird'

constraints
1 < n < 100
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n > 0 and n <= 100:
        if n % 2 == 1:
            print('Weird')
        elif n % 2 == 0 and n >= 2 and n <= 5:
            print('Not Weird')
        elif n % 2 == 0 and n >= 6 and n <=20:
            print('Weird')
        elif n % 2 == 0 and n > 20:
            print('Not Weird')