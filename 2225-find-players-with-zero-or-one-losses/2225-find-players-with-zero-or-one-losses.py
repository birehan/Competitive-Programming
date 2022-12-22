class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        for win, lose in matches:
            dic[win] = dic.get(win, 0) 
            dic[lose] = 1 + dic.get(lose, 0)
        
        winner, one_lose = [], []
        for key, value in dic.items():
            if value == 0:
                winner.append(key)
            elif value == 1:
                one_lose.append(key)
            
        winner.sort()
        one_lose.sort()

        return [winner, one_lose]
