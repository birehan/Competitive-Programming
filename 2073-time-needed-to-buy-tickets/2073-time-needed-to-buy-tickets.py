class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        for index, time in enumerate(tickets):
            if index <= k:
                total += min(tickets[k], time)
            else:
                total += min(tickets[k]-1, time)
        
        return total