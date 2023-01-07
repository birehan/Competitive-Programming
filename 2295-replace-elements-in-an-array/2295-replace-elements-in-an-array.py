class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic_value = {}
        for index, value in enumerate(nums):
            dic_value[value] = index

        for to_remove, new_value in operations:
            nums[dic_value[to_remove]] = new_value
            dic_value[new_value] = dic_value.pop(to_remove)

        return nums