class Solution:
    def compute(self, num1, num2, operation):
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        else:
            return math.trunc(num1/num2)
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric() or (token[0]=="-" and len(token) > 1):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                value = self.compute(num1, num2, token)
                stack.append(value)
        
        return stack[0]
       

