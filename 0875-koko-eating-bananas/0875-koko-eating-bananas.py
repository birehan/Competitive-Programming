class Solution:
    def validate(self, piles, h, speed):
        total = 0
        for pile in piles:
            total += ceil(pile/speed)
        return total <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 0, max(piles) + 1

        while right > left + 1:
            mid = (right + left) // 2
            if self.validate(piles, h, mid):
                right = mid
            else:
                left = mid
        
        return right