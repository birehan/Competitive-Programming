#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            unsorted = arr[i]

            for j in range(i, 0, -1):
                if (unsorted < arr[j - 1]):
                    arr[j] = arr[j - 1]
                    print(*arr)

                else:
                    arr[j] = unsorted
                    print(*arr)
                    break
                if ((unsorted < arr[j - 1]) and (j - 1 == 0)):
                    arr[j - 1] = unsorted
                    print(*arr)
    return


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
