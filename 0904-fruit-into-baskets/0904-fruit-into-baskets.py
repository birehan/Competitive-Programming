class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        store = defaultdict(int)
        left = max_len = 0

        for right, num in enumerate(fruits):
            store[num] += 1
            if left < right and len(store.keys()) > 2:
                store[fruits[left]] -= 1
                if not store[fruits[left]]:
                    del store[fruits[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
       
        return max_len