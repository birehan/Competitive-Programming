class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        index = 0

        while index < len(s):
            # if character 
            if s[index].isalpha():
                result.append(s[index])
                index += 1   

            # when getting numbers
            elif s[index].isnumeric():
                num = []
                while index < len(s) and s[index].isnumeric():
                    num.append(s[index])
                    index += 1
                
                values = []
                opening = 0
                index += 1

                # move till the closing of the bracket
                while index < len(s) and (s[index] != "]" or opening != 0):
                    values.append(s[index])
                    opening += 1 if s[index] == "[" else 0
                    opening -= 1 if s[index] == "]" else 0
                    index += 1

                # recursive call
                v = list(self.decodeString("".join(values)))
                result.extend(v*int("".join(num))) 
                index += 1

        
        return "".join(result)
