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
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            index = i+1 
            cur = arr[index]
            while index > 0 and arr[index-1] > cur:
                arr[index] = arr[index-1] 
                print(*arr)
                index -= 1
            arr[index] = cur
            print(*arr)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
