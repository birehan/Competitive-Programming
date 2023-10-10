class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dire = [0, 1]
        pos = [0, 0]
        move = {"L": 0, "R": 1}


        for inst in instructions:
            if inst == "G":
                pos[0] += dire[0]
                pos[1] += dire[1]
            else:
                dire = dire[::-1]
                dire[move[inst]] *= -1
     
        
        if dire == [0, 1] and (pos != [0, 0]):
            return False
                
        return True