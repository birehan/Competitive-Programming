class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        values = [0] * len(persons)
        freq = defaultdict(int)
        cur_max = 0

        for i in range(len(persons)):
            freq[persons[i]] += 1
            if freq[cur_max] <= freq[persons[i]]:
                cur_max = persons[i]

            values[i] = cur_max
        
        self.values = values
        
    def q(self, t: int) -> int:

        left, right = -1, len(self.times)

        while right > left + 1:
            mid = (left + right)//2
            if self.times[mid] > t:
                right = mid
            else:
                left = mid

        return self.values[left]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)