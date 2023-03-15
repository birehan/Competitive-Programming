class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        self.isValid = False
        def backtrack(num,arr):
            
            if num=="":
                if not self.isValid and len(arr)>2:
                    self.isValid = True
                    
            candidates = [i for i in range(1,len(num)+1)]

            for candidate in candidates:
                intVal = num[:candidate]
                if (len(intVal)==len(str(int(intVal)))) and (len(arr)<2 or arr[-1]+arr[-2] == int(intVal)):
                    arr.append(int(intVal))
                    backtrack(num[candidate:],arr)
                    arr.pop()
        
        
        
        backtrack(num,[])
        return self.isValid