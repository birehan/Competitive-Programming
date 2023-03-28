class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        index = 0

        while index < len(nums):
            connect = nums[index] - 1

            if connect != index:
                if nums[index] == nums[connect]:
                    return nums[index]

                nums[index], nums[connect] = nums[connect], nums[index]
            else:
                index += 1