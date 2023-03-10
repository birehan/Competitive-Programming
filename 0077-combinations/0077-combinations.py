class Solution:
    def helper(self, n, k, point, cur):
        if point > n:
            return

        if len(cur) == k:
            self.answer.append(cur.copy())
            return
        
        cur.add(point)
        self.helper(n, k, point+1, cur)
        cur.remove(point)
        self.helper(n, k, point+1, cur)


    def combine(self, n: int, k: int) -> List[List[int]]:
        self.answer = []
        self.helper(n+1, k, 1, set())
        return self.answer