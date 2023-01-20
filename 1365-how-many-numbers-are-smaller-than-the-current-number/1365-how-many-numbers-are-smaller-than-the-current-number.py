class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums = [[nums[i], i] for i in range(len(nums))]
        nums.sort()
        answer = [0] * len(nums)
        for index, pair in enumerate(nums):
            if index > 0 and nums[index][0] == nums[index-1][0]:
                answer[pair[1]] = answer[nums[index-1][1]]
            else:
                answer[pair[1]] = index

        return answer

        