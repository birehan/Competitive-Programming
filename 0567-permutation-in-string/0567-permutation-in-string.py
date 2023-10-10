class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        left = 0

        for right, st in enumerate(s2):
            if st in counter:
                counter[st] -= 1
            
            if right - left + 1 == len(s1):
                if all(v == 0 for v in counter.values()):
                    return True

                if s2[left] in counter:
                    counter[s2[left]] += 1
                
                left += 1
        
        return False