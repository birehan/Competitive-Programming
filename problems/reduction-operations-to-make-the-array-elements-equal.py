class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = list(Counter(nums).items())

        cost = 0
        for i in range(len(count)-1, 0, -1):
            cost += count[i][1]
            count[i-1] = (1, count[i][1] + count[i-1][1])
        
        return cost


        #     
        #    
        # 
        #    