class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = index = 0         
        for i in range(len(nums)):
            if nums[i] == target:
                count += 1
            if nums[i] < target:
                index += 1

        res = []
        for i in range(count):
            res.append(i+index)  

        return res