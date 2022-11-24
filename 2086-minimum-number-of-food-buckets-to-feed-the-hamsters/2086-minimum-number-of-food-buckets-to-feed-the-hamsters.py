class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        min_food = 0
        hamsters = [None] +  list(hamsters) + [None]
        for i in range(1, len(hamsters)-1):
            if hamsters[i] == 'H':
                if hamsters[i-1] == "F":
                    continue 
                elif hamsters[i+1] == '.':
                    hamsters[i+1] = "F"
                    min_food += 1
                elif hamsters[i-1] == '.':
                    min_food += 1
                else: return -1
        
        return min_food

