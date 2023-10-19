class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costs = [[1, costs[0]], [7, costs[1]], [30, costs[2]]]
        
        @cache
        def dfs(index):
            if index >= len(days):
                return 0

            
            total = inf
            for travel_day, cost in costs:
                next_index = bisect_left(days, days[index] + travel_day)
                total = min(total, cost + dfs(next_index))
            
            return total

        return dfs(0)


