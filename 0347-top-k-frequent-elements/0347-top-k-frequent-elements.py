class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequency = [[] for _ in range(len(nums))]

        for key, freq in counter.items():
            frequency[freq-1].append(key)

        answer = []
        for i in range(len(frequency)-1, -1, -1):
            for key in frequency[i]:
                answer.append(key)
                if len(answer) == k:
                    return answer
        
        return answer