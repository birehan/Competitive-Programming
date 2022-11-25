# User function Template for python3

class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        # code here
        root = i
        left = (i * 2) + 1
        right = (i * 2) + 2

        if left < n and arr[root] < arr[left]:
            left, root = root, left

        if right < n and arr[root] < arr[right]:
            right, root = root, right

        if root != i:
            arr[root], arr[i] = arr[i], arr[root]
            self.heapify(arr, n, root)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        # code here

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        # code here


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr, n)
        print(*arr)

# } Driver Code Ends