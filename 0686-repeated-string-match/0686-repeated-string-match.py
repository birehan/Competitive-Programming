class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        pi = [0] * len(b)

        index, pointer = 1, 0
        while index < len(b):
            if b[index] == b[pointer]:
                pi[index] = pointer + 1
                index += 1
                pointer += 1
            elif pointer == 0:
                index += 1
            else:
                pointer = pi[pointer -1]
        
        index = pointer = 0
        total = 0
        n = max(len(a), len(b)) * 2
        
        while total < n:
            if a[index] == b[pointer]:
                total += 1
                index = (index + 1) % len(a) 
                pointer += 1
            elif pointer == 0:
                index = (index + 1) % len(a)
                total += 1 
            else:
                pointer = pi[pointer - 1]

            if pointer == len(b):
                return ceil(total/len(a))
    
        return -1

        