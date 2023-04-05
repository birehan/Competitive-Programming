class Solution:
    def helper(self, bit, n, index):
        if index == n:
            self.count += 1
            return

        for i in range(n):
            cur = 1 << i
            if not cur & bit:
                if ((i+1) % (index + 1) == 0) or ((index + 1) % (i + 1) == 0):
                    self.helper(bit | cur, n, index + 1)

    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.helper(0, n, 0)
        return self.count