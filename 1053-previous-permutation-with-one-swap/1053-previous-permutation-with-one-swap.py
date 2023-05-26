class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        smallest = len(arr)-1
        ith = None

        for i in range(len(arr)-2, -1, -1):
            if arr[smallest] < arr[i]:
                ith = i
                break
            else:
                smallest = i
        
        if ith != None:
            for i in range(smallest+1, len(arr)):
                if arr[i] > arr[smallest] and arr[i] < arr[ith]:
                    smallest = i
            
            arr[smallest], arr[ith] = arr[ith], arr[smallest]
        
        return arr