class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        string = "\n".join(source)
        index, length = 0, len(string)
        result = ""
        
        
        while index < length:
            cur = string[index:index+2]
            if cur == "//":
                while index < length and string[index] != "\n":
                    index += 1
            elif cur == "/*":
                index += 2
                while string[index:index+2] != "*/":
                    index += 1
                index += 2
            else:
                result += string[index]
                index += 1
        
        result = [line for line in result.split("\n") if line]
        return result