class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        result = sorted(dic.items(), key = lambda x:x[1])
        answer = [result[i][0] for i in range(len(result)-k, len(result))]
        return answer

