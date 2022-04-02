#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    position = 0
    isValley = False
    valley = 0
    for i in range(steps):
        if path[i] == 'U':
            position += 1
        else:
            position -= 1

        if position > 0:
            isValley = False
        elif position == 0 and isValley:
            valley += 1
        elif position < 0:
            isValley = True
    return valley

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
