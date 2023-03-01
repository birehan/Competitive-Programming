class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # choosing the optimal every time
        # player 1 is positive and player 2 negative
        # return -v

        @cache
        def helper(left, right, turn):
            if left == right:
                return turn * nums[left]

            left_value = nums[left] * turn
            left_value += helper(left+1, right, turn * -1)

            right_value = nums[right] * turn
            right_value += helper(left, right-1, turn * -1)

            result = max(left_value, right_value) if turn == 1 else min(left_value, right_value)

            return result
            
        result = helper(0, len(nums)-1, 1)
    
        return result >= 0



