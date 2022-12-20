class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary) - min(salary) - max(salary)
        return total/(len(salary)-2)