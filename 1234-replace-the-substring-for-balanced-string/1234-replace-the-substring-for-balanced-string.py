class Solution:
    def validate(self, counter, length):
        for key, value in counter.items():
            if value > length:
                return False
        return True

    def balancedString(self, s: str) -> int:
        counter_1 = Counter(s)
        left, length = 0, len(s)//4
        if self.validate(counter_1, length):
            return 0

        counter_2 = Counter()
        min_length = inf

        for right, string in enumerate(s):
            counter_2[string] += 1
            while self.validate(counter_1 - counter_2, length):
                min_length = min(right-left+1, min_length)
                counter_2[s[left]] -= 1
                left += 1
        
        return min_length         