class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        dic[(0, 0)] = 1


        for i in range(1, len(nums)):
            for j in range(i):
                sign = 0
                if nums[i] > nums[j]:
                    sign = 1
                elif nums[i] < nums[j]:
                    sign = -1
                
                if sign != 0:
                    value = 1 + dic.get((j, sign * -1), 1)
                    dic[(i, sign)] = max(dic[(i, sign)], value)
            
        
        return max(dic.values())

        