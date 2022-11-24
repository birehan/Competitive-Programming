class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        before = [0] * len(security)
        after = [0] * len(security)

        for i in range(1, len(security)):
            if  security[i] <= security[i-1]:
                before[i] = 1 + before[i-1]

            if security[-i-1]  <= security[-i]:
                after[-i-1] = 1 + after[-i]
        
        answer = []
        for i in range(len(security)):
            if before[i] >= time <= after[i]:
                answer.append(i)
        
        return answer