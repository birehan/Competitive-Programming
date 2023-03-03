class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        mid_len = (2**(n-2))
        new_k = k if k <= mid_len else k - mid_len
        prev_val = self.kthGrammar(n-1, new_k)

        if k <= mid_len:
            return prev_val
        else:
            return prev_val ^ 1

    # 