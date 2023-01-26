class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        cur = 0
        index = (cur + k) % (len(nums))
       
        for i in range(len(nums)):
            if index == cur:
                cur += 1
                index = (cur + k) % (len(nums))
            else:
                nums[index], nums[cur] = nums[cur], nums[index]
                index = (index + k) % (len(nums))
          