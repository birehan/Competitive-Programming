class Solution:
    def result(self, rowIndex, result):
        if rowIndex == 0:
            return result

        for i in range(len(result)-1, 0, -1):
            result[i] += result[i-1]
        result.append(1)
        return self.result(rowIndex-1, result)

    def getRow(self, rowIndex: int) -> List[int]:
        return self.result(rowIndex, [1])
        
       