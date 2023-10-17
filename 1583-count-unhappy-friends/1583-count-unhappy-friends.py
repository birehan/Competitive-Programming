class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        prior = defaultdict(list)
        for a, b in pairs:
            prior[a] = preferences[a][:preferences[a].index(b)]
            prior[b] = preferences[b][:preferences[b].index(a)]
        
        count = 0
        for a in prior:
            for b in prior[a]:
                if a in prior[b]:
                    count += 1
                    break
        
        return count



