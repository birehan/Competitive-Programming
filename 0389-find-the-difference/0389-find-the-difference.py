class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dic = Counter(s)
        t_dic = Counter(t)

        res = ""
        for k, v in t_dic.items():
            res  += k * (v - s_dic.get(k, 0))
        
        return res

        