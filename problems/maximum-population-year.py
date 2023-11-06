class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        values = [0] * 102
        offset = 1950


        for a, b in logs:
            values[a - offset] += 1
            values[b - offset] -= 1
        
        max_pop = 0

        for i in range(1, len(values)):
            values[i] += values[i-1]
            if values[i] > values[max_pop]:
                max_pop = i

        
        
        return max_pop + offset
        