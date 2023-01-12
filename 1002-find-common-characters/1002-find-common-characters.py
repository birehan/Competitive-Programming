class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = Counter(words[0])
        for i in range(1, len(words)):
            word = Counter(words[i])
            for k, v in dic.items():
                value = min(v, word.get(k, 0))
                dic[k] = value
        
        answer = []
        for k, v in dic.items():
            if v: answer.extend( [k] * v)
        
        return answer
       