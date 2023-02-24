class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        pairs.sort(reverse=True)

        fleets = []
        for pos, spe in pairs:
            time = (target-pos)/spe
            if not fleets or fleets[-1] < time:
                fleets.append(time)
        
        return len(fleets)