#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return " ".join(map(lambda s : s[0:].capitalize() , s.split(" ")))

if __name__ == '__main__':

    s = input()

    result = solve(s)