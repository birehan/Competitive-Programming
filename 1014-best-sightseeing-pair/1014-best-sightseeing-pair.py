class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left = values[0] - 1
        max_score = 0
        for right in range(1, len(values)):
            max_score = max(max_score, values[right] + left)
            left = max(values[right], left) - 1

        return max_score

        # 8, 1, 5, 2, 6