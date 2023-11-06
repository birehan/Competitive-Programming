class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for right in range(len(nums)):
            cur = target-nums[right]
            if cur in dic:
                return [dic[cur], right]
            dic[nums[right]] = right
            