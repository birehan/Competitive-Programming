class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        is_inc = None
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            elif arr[i] > arr[i-1]:
                if is_inc == False:
                    return False
                is_inc = True
            else:
                if is_inc == None:
                    return False
                is_inc = False
        return is_inc == False