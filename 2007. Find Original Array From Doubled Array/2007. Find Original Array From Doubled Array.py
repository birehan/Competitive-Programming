from collections import Counter


class Solution(object):
    def findOriginalArray(self, changed):
        if len(changed) < 2 or len(changed) % 2 != 0:
            return []

        counter = Counter(changed)
        changed.sort()
        result = []
        for i in changed:
            if i == 0:
                if counter[i] > 1:
                    counter[i] -= 2
                    result.append(i)
            elif counter[i] and counter[i * 2]:
                result.append(i)
                counter[i], counter[i * 2] = counter[i] - 1, counter[i * 2] - 1

        if len(result) != len(changed) // 2:
            return []

        return result

        """
        :type changed: List[int]
        :rtype: List[int]
        """
