class Solution:
    def interpret(self, command: str) -> str:
        index = 0
        res = ""
        while index < len(command):
            if command[index] == "(":
                if index+1 < len(command) and command[index+1] == ")":
                    res += "o"
                    index += 2
                else: 
                    res += "al"
                    index += 4
            else:
                res += "G"
                index += 1
        
        return res
