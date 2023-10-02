class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        self.min_cost = inf

        @cache
        def helper(a, b):
            index = a + b
            if index >= len(costs):
                return 0
            
            a_cost = b_cost = inf
            if a < n:
                 a_cost = costs[index][0] + helper(a+1, b)
            
            if b < n:
                b_cost = costs[index][1] + helper(a, b + 1)
            
            return min(a_cost, b_cost)
        
        return helper(0, 0)
