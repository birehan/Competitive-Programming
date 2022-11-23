class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * 10001
        for numPassengersi, fromi, toi in trips:
            passengers[fromi] += numPassengersi
            passengers[toi] -= numPassengersi
        
        total_passengers = 0
        for i in passengers:
            total_passengers += i
            if total_passengers > capacity:
                return False
        
        return True
        