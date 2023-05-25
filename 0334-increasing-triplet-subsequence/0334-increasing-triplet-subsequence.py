class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        smallest_num = nums[0]
        smallesst_pair = None

        for i in range(1, len(nums)):
            if smallesst_pair != None and nums[i] > smallesst_pair:
                return True

            if nums[i] < smallest_num:
                smallest_num = nums[i]
            elif  nums[i] > smallest_num:
                if smallesst_pair == None or smallesst_pair > nums[i]:
                    smallesst_pair = nums[i]

        
        return False


        