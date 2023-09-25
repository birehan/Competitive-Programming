class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        sorted_scores = sorted([[ages[i], scores[i]] for i in range(n)])
        max_score = 0
        dp = [0] * n

        for i in range(n):
            cur_score = sorted_scores[i][1]
            max_neghbor = 0
            for j in range(i-1, -1, -1):
                if sorted_scores[j][1] <= sorted_scores[i][1]:
                    max_neghbor = max(max_neghbor, dp[j])
            

            dp[i] = sorted_scores[i][1] + max_neghbor
            
            max_score = max(max_score, dp[i])
        
        return max_score

