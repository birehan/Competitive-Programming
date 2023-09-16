class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        store = [(-j, i) for i, j in counter.items()]
        heapify(store)
        res = ""
        while len(store) > 1:
            x = heappop(store)
            y = heappop(store)
           
            res += x[1] + y[1]
            if x[0] < (-1):
                heappush(store, (x[0]+1, x[1]))
            if y[0] < (-1):
                heappush(store, (y[0]+1, y[1]))
        
        if store and store[0][0] < -1:
            return ""


        return res + store[0][1] if store else res