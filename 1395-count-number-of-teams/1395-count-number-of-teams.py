class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)
        greater = [0] * n
        smaller = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    greater[i] += 1
                elif rating[i] > rating[j]:
                    smaller[i] += 1

        
        for i in range(n):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    count += greater[j]
                elif rating[i] > rating[j]:
                    count += smaller[j]
        
        return count

