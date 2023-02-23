class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = defaultdict(int)
        left = 0
        for right, string in enumerate(s2):
            count2[string] += 1
            if count1 == count2:
                return True
            if right - left + 1 == len(s1):
                count2[s2[left]] -= 1
                if not count2[s2[left]]:
                    del count2[s2[left]]
                left += 1
        
        return False