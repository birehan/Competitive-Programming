class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {key:index for index, key in enumerate(s)}
        left = last_position = 0
        answer = []
        
        for right, letter in enumerate(s):
            last_position = max(last_position, dic[letter])
            if last_position == right:
                answer.append(right-left+1)
                left = right + 1
        
        return answer
        

