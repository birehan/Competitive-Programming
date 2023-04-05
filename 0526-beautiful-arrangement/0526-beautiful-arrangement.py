class Solution:
    def countArrangement(self, n: int, bit=0, index =0 ) -> int:
        if index == n:
            return 1
        
        count = 0
        for i in range(n):
            cur = 1 << i
            if not cur & bit:
                if ((i+1) % (index + 1) == 0) or ((index + 1) % (i + 1) == 0):
                    count += self.countArrangement(n, bit | cur, index + 1)

        return count