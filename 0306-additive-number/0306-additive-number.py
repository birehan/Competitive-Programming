class Solution:
    def validate(self, values):
        if int(values[0]) + int(values[1]) != int(values[2]):
            return False
        for value in values:
            if len(value) != len(str(int(value))):
                return False
        return True
        
    def helper(self, num1, num2, index):
        if index == len(self.num):
            return
        
        cur = ""
        for i in range(index, len(self.num)):
            cur += self.num[i]

            if not num1:
                self.helper((cur), num2, i+1)

            elif not num2:
                self.helper(num1, (cur), i+1)
                
            elif self.validate([num1, num2, cur]):
                if i+1 == len(self.num):                   
                    self.answer = True
                self.helper(num2, (cur), i+1)

            elif int(cur) > int(num1) + int(num2):
                return 
            

            
    def isAdditiveNumber(self, num: str) -> bool:
        self.answer = False
        self.num = num
        self.helper("", "", 0)
        return self.answer 