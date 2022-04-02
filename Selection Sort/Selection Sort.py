class Solution:
    def select(self, arr, i):
        # code here
        smallest = i
        for j in range(i + 1, len(arr), 1):
            if arr[j] < arr[smallest]:
                smallest = j
        return smallest

    def selectionSort(self, arr, n):
        # code here
        for i in range(n):
            smallest = self.select(arr, i)
            arr[i], arr[smallest] = arr[smallest], arr[i]

        return arr