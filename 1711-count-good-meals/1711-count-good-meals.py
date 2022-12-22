class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = Counter(deliciousness)

        powers_2 = [1] 
        for i in range(20):
            cur = powers_2[-1] * 2
            powers_2.append(cur)
        
        total = 0
        for cur, cur_freq in freq.items():
            index = bisect_left(powers_2, cur)
            diff =  powers_2[index] - cur

            if cur and  diff in freq:
                total += freq[diff] * cur_freq
                    
            if cur and diff == 0:
                total += (cur_freq* (cur_freq-1))//2
           

        total = total % (10**9 + 7)
        return total

























