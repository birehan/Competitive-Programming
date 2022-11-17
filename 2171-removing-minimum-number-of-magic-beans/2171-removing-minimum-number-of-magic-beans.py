class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        max_value = 0
        for index, bean in enumerate(sorted(beans)):
            max_value = max(max_value, bean*(len(beans)-index))
        return sum(beans) - max_value
