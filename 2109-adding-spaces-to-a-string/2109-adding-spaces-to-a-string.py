class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        s_index = 0
        for index, val in enumerate(s):
            if s_index < len(spaces) and index == spaces[s_index]:
                res.append(" ")
                s_index += 1
            res.append(val)

        return "".join(res)