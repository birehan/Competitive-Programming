class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(bit):
            on_bits = sum(map(int, bin(bit)[2:]))
            if on_bits == n:
                return 0
            
            index = (on_bits//2) + 1
            max_v = 0
            for i in range(n):
                if not bit & 1 << i:
                    bit =  bit ^ 1 << i
                    for j in range(i + 1, n):
                        if not bit & 1 << j:
                            bit =  bit ^ 1 << j
                            max_v = max(max_v, dfs(bit) + gcd(nums[i], nums[j]) * index)
                            bit =  bit ^ 1 << j
                        
                    bit =  bit ^ 1 << i
            
            return max_v
        

        return dfs(0)
                    
        