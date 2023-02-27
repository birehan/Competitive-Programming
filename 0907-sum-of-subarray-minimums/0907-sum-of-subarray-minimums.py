class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        count = [0] * len(arr)
        stack = []
        for index, value in enumerate(arr):
            while stack and stack[-1][0] > value:
                v, i = stack.pop()
                times  = (count[i])//(len(arr)-i)
                count[index] += (len(arr)-index) * times
                count[i] -= (len(arr)-index) * times
                
            stack.append((value, index))
            count[index] += len(arr)-index
           

        res = 0
        for i in range(len(count)):
           res += count[i] * arr[i]
        
        return (res % (10**9 + 7))