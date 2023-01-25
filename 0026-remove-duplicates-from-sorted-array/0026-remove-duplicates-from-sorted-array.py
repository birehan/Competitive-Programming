class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = -1
        for i in range(len(nums)):
            if pointer == -1 or nums[pointer] != nums[i]:
                nums[pointer+1] = nums[i]
                pointer += 1

        return pointer + 1