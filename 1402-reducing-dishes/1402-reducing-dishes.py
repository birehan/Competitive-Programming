class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        max_sum = 0
        value_sum = cur_sum = 0
        
        for i in range(len(satisfaction)-1, -1, -1):
            cur_sum += satisfaction[i] + value_sum
            
            if cur_sum <= max_sum:
                return max_sum
            
            value_sum += satisfaction[i]
            max_sum = cur_sum
            
        
        return max_sum

            

        