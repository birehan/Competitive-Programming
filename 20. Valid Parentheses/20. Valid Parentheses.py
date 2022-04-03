class Solution(object):
    def isValid(self, s):
        dictionary = {"(": ")", "[": "]", "{": "}"}
        list = []
        for character in s:
            if character in dictionary:
                list.append(character)
            else:
                if len(list) != 0:
                    if character != dictionary[list.pop()]:
                        return False
                else:
                    return False
        if len(list) != 0:
            return False
        return True
