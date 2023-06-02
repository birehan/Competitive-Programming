class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = defaultdict(int)
        max_value = 0

        for i in range(len(questions)):
            max_value = max(max_value, dp[i])
            pointi, poweri = questions[i]
            dp[i+poweri+1] = max(dp[i+poweri+1], pointi + max_value) 
           

        
        return max(dp.values())


        