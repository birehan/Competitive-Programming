class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        inc, left = False, None
        max_length = 0

        for right in range(1, len(arr)):
            cur = arr[right] - arr[right - 1]
            if cur == 0:
                inc = False
                left = None

            if cur > 0 and not inc:
                left = right-1
                inc = True

            if cur < 0:
                inc = False
                if left != None and (right-left+1) > 2:
                    max_length = max(max_length, right-left+1)
            
        
        return max_length


        
