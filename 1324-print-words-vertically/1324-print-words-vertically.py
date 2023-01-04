from itertools import zip_longest
class Solution:
    def printVertically(self, s: str) -> List[str]:
        v_words = []
        array = s.split()
        max_length = max(array, key=len)
        for i in range(len(max_length)):
            cur = []
            for j in range(len(array)):
                if i < len(array[j]):
                    cur.append(array[j][i])
                else: cur.append(" ")
        
            v_words.append("".join(cur).rstrip())

        return v_words
