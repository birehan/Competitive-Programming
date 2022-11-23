class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n 
        for left, right, seats in bookings:
            answer[left-1] += seats
            if right < n:
                answer[right] -= seats
        answer = list(accumulate(answer))
        return answer
        