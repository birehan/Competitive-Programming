class Solution(object):
    def fizzBuzz(self, n):
       list=[]
       for i in range(1, n+1):
            if i%5 == 0 and i%3==0:
                list.append("FizzBuzz")
            elif i % 5 ==0:
                list.append("Buzz")
            elif i % 3 ==0:
                list.append("Fizz")
            else:
                list.append(str(i))
       return list