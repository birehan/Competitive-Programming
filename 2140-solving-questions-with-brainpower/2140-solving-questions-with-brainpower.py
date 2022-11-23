class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        DP = [0] * (N+1)
        for i in range(N-1, -1, -1):
            p, b = questions[i]
            DP[i] = max(p + DP[min(N, i + b + 1)], DP[i+1])
        return DP[0]