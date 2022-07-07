class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        left = 0
        right = firstLen
        max_sum = 0

        while right <= len(nums):
            sub_array_1 = nums[left: right]
            sum_1 = sum(sub_array_1)

            left_1 = 0
            right_1 = secondLen
            values = []

            while right_1 <= left:
                sub_array_2_left = nums[left_1: right_1]
                values.append(sum(sub_array_2_left))
                left_1 += 1
                right_1 += 1

            left_2 = right
            right_2 = secondLen + left_2

            while right_2 <= len(nums):
                sub_array_2_right = nums[left_2:right_2]
                values.append(sum(sub_array_2_right))
                left_2 += 1
                right_2 += 1
            sum_2 = max(values) if values else 0
            if sum_1 + sum_2 > max_sum:
                max_sum = sum_1 + sum_2

            left += 1
            right += 1

        return max_sum
