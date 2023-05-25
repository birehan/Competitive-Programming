class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        holding = {5:0, 10:0, 20: 0}

        for bill in bills:
            if bill == 5:
                holding[bill] += 1
            
            elif bill == 10:
                if not holding[5]:
                    return False
                holding[bill] += 1
                holding[5] -= 1
            elif bill == 20:
                if holding[5]  and holding[10]:
                    holding[5] -= 1
                    holding[10] -=1
                elif holding[5] > 2:
                    holding[5] -= 3
                else:
                    return False
        
        return True
                
        