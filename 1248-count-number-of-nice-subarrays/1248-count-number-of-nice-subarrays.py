class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        cur_odd = 0
        count = 0
        for num in nums:
            cur_odd += 1 if num%2==1 else 0
            if cur_odd-k in dic:
                count += dic[cur_odd - k]
            
            dic[cur_odd] += 1

        return count