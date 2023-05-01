class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        
        answer = ""
        
        if x < 0:
            answer += "-"
            x = -x
            
        while x != 0:
            if (x % 10) != 0 or (answer != "" or answer != "-"):
                answer += str(x % 10)
            
            x = x // 10
                    
        return int(answer) if ((-2 ** 31) <= int(answer) <= ((2**31) -1)) else 0
            
            