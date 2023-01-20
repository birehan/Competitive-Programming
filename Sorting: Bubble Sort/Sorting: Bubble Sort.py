#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swap_number = 0
    for n in range(len(a), 0, -1):
        for i in range(n):
            if (n > 1) and (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swap_number += 1
            n -= 1

    print("Array is sorted in " +  str(swap_number) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
    return

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
