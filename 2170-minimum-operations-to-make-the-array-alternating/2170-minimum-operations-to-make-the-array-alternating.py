class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
            
        even_count, odd_count = defaultdict(int),  defaultdict(int)

        for i in range(len(nums)):
            if i % 2 == 0:
                even_count[nums[i]] += 1
            else:
                odd_count[nums[i]] += 1
        
        even_count = sorted(even_count.items(), key=lambda x: x[1], reverse=True)
        odd_count = sorted(odd_count.items(), key=lambda x: x[1], reverse=True)
        saved = 0

        if even_count[0][0] == odd_count[0][0]:
            if len(even_count) > 1 and len(odd_count) > 1:
                saved = max(even_count[0][1] + odd_count[1][1], odd_count[0][1] + even_count[1][1])
            elif len(even_count) == 1 and len(odd_count) > 1:
                saved = even_count[0][1]+ odd_count[1][1]
            elif len(odd_count) == 1 and len(even_count) > 1:
                saved = odd_count[0][1] + even_count[1][1]
            else:
                saved = max(odd_count[0][1], even_count[0][1])
        else:
            saved = even_count[0][1] +  odd_count[0][1]

        return len(nums) - saved
        