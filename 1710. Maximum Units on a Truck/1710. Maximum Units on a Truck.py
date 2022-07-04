from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])
        summ = 0
        while truckSize > 0 and boxTypes:
            box = boxTypes.pop()
            if truckSize > box[0]:
                truckSize -= box[0]
                summ += box[0] * box[1]

            else:
                summ += truckSize * box[1]
                truckSize -= truckSize

        return summ

