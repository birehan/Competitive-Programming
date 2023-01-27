class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def swap(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        flip = []
        for i in range(len(arr), 1, -1):
            cur_max = max(arr[:i])
            index_max = arr.index(cur_max) 

            flip.extend([index_max + 1, i])
            swap(0, index_max)
            swap(0, i-1)
            
        return flip