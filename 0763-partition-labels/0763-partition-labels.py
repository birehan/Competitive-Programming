class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer = []
        total = ""
        for index, letter in enumerate(s):
            if letter not in total:
                answer.append(letter)
            else:
                while len(answer) > 1 and letter not in answer[-1]:
                    last = answer.pop()
                    answer[-1] += last
                answer[-1] += letter
            total += letter


        answer = [len(i) for i in answer]
       
        return answer
            
            

