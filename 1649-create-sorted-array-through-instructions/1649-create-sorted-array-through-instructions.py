class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        order = []
        
        ans = 0
        for i, a in enumerate(A):
            l, r = bisect.bisect_left(order, a), bisect.bisect(order, a)
            ans += min(l, i-r)
          
            order[r:r] = [a] # AC
            
        return ans % MOD 