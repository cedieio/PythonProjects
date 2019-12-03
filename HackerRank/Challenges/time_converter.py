#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hourVal = 0
    minuteVal = 0
    secondVal = 0

    valList = s.split(':')

    
    if int(valList[1]) >= 0 and int(valList[1]) <= 59:
        minuteVal = int(valList[1])
    if int(valList[2][:len(valList[2]) - 2]) >= 0 and int(valList[2][:len(valList[2]) - 2]) <= 59:
        secondVal = int(valList[2][:len(valList[2]) - 2])
    if int(valList[0]) >= 1 and int(valList[0]) <= 12:
        hourVal = int(valList[0])
        if len(valList) == 3 and len(valList[2]) >= 3:
            if valList[2][-2:] == 'PM' and hourVal < 12:
                hourVal = hourVal + 12
            elif valList[2][-2:] == 'AM' and hourVal == 12:
                hourVal = 0
                          
    strVal = '{0:02d}:{1:02d}:{2:02d}'.format(hourVal,minuteVal,secondVal)
    print(strVal)
    return strVal

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

