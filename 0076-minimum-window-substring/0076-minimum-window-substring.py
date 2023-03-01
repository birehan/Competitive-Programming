class Solution:
    # validate if all t in s count of the window
    def validate(self, s_counter, t_counter):
        for key, value in t_counter.items():
            if key not in s_counter or s_counter[key] < value:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        s_counter = defaultdict(int)
        left = 0
        min_string = ()
        min_window = inf

        for right, string in enumerate(s):
            s_counter[string] += 1

            while self.validate(s_counter, t_counter):
                if min_window > right-left+1:
                    min_string = (left, right+1)
                    min_window = right-left+1

                s_counter[s[left]] -= 1
                left += 1
        
        if min_window == inf:
            return ""

        return "".join(s[min_string[0]: min_string[1]])        
        


