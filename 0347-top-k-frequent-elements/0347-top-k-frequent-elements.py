class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = [[] for i in range(len(nums)+1)] 
        counter = Counter(nums)
        for key, value in counter.items():
            store[value].append(key)
        
        answer = []
        
        for i in range(len(store)-1, -1, -1):
            for j in range(len(store[i])):
                answer.append(store[i][j])
                if len(answer) == k:
                    return answer
       