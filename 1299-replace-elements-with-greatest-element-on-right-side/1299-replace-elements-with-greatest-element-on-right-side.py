class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last = -1
        for i in range(len(arr), 0, -1):
            arr[i-1], last = last, max(last, arr[i-1])
        
        return arr