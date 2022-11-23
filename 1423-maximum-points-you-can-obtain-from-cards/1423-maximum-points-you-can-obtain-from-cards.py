class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        right = len(cardPoints)-k
        cur_sum = sum(cardPoints[right:])
        max_point = cur_sum
        for left in range(k):
            cur_sum += cardPoints[left] - cardPoints[right]
            max_point = max(max_point, cur_sum)
            right += 1
        
        return max_point