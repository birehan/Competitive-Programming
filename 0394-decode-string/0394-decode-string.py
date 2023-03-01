class Solution:
    def decodeString(self, s: str) -> str:
        self.index = 0
        def helper(result, times):

            # base case

            while self.index < len(s) and s[self.index].isalpha():
                result.append(s[self.index])
                self.index += 1

            if self.index < len(s) and s[self.index] == "]":
                self.index += 1
                return times * result

            num = []
            while self.index < len(s) and s[self.index].isnumeric():
                num.append(s[self.index])
                self.index += 1
            
            if num:
                self.index += 1
                # print(num, result)

                v = helper([], int("".join(num)))
                result.extend(v)
                # print(result)
            if self.index < len(s):
                return helper(result, times)
                
            return result * times

            

        return "".join(helper([], 1))

