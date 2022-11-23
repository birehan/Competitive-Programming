class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        left_over =  k % sum(chalk)
        chalk = list(accumulate(chalk))
        return bisect.bisect(chalk, left_over)
        