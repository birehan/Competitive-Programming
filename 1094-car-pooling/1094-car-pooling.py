class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0] * 10001

        for numPassengersi, fromi, toi in trips:
            locations[fromi] += numPassengersi
            locations[toi] -= numPassengersi
        
        total = 0
        for passengers in locations:
            total += passengers
            if total > capacity:
                return False
        
        return True






        