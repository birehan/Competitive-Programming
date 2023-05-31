class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        def compute_sum(index):
            start = 1
            summ = 0
            for i in range(index, len(satisfaction)):
                summ += start * satisfaction[i]
                start += 1
            
            return summ
        
        zero_ind = bisect_left(satisfaction, 0)
        max_sum = compute_sum(zero_ind)

        while zero_ind:
            zero_ind -= 1
            cur_sum = compute_sum(zero_ind)
            if cur_sum <= max_sum:
                return max_sum

            max_sum = cur_sum
            
        
        return max_sum

            

        