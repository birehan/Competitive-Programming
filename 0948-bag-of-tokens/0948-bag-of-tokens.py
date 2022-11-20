class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        max_score = score = 0
        left, right = 0, len(tokens)-1

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                max_score = max(max_score, score)
                left += 1
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else: break
        
        return max_score