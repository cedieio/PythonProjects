
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    #return len([x for x in ar if x == max(ar)]) <-- super slow with big ints
    greatestVal = max(ar)
    count = 0
    for v in ar:
        if v == greatestVal:
            count = count+1
    return count
if __name__ == '__main__':
    

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(result)


