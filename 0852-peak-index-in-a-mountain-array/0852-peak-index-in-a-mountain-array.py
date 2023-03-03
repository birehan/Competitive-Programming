class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr)-2
        while right > left:
            mid = (right+left)//2
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid + 1
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                right = mid -1 
            else:
                return mid
        return right
