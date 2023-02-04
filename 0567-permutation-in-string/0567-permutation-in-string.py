class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = Counter(s1)
        compare = Counter()
        left = 0
        for right, string in enumerate(s2):
            compare[string] += 1
            if compare == dic:
                return True
            if right-left+1 == len(s1):
                compare[s2[left]] -= 1
                left += 1

        return False
    