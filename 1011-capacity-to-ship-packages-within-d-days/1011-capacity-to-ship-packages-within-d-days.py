class Solution:
    def validate(self, weights, capacity, days):
        day_count = 0
        cur_sum = 0
        for weight in weights:
            if cur_sum + weight  > capacity:
                day_count += 1
                cur_sum = 0

            cur_sum += weight
        return day_count+1 <= days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = 0, sum(weights)
        while right > left + 1:
            mid = (right+left)//2
            if self.validate(weights, mid, days):
                right = mid
            else:
                left = mid

        return max(right, max(weights))