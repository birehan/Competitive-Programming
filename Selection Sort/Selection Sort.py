#User function Template for python3

class Solution: 
    def select(self, arr, i):
        selected = i
        for j in range(i, len(arr)):
            if arr[selected] > arr[j]:
                selected = j
        return selected
        # code here 
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            selected = self.select(arr, i)
            arr[selected], arr[i] = arr[i], arr[selected]
        
        return arr
