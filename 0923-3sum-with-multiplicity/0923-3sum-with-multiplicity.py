class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        arr = sorted(list(set(arr)))
        count = 0

        for i in range(len(arr)):
            left, right = i+1, len(arr)-1
            freq = counter[arr[i]]
            while left < right:
                cur_sum = arr[i] + arr[left] + arr[right]
                if cur_sum == target:
                    count += (freq * counter[arr[left]] * counter[arr[right]])
                    left += 1
                    right -= 1
                elif cur_sum < target: left += 1
                else: right -= 1

            if counter[arr[i]] > 1:
                remaining = target -  (arr[i] * 2)
                if arr[i] != remaining and remaining in counter:
                    count += (freq*(freq-1))//2 * counter[remaining]

            if freq > 2 and  (arr[i] * 3 == target):
                count += freq * ((freq -1) * (freq-2))//6
        
        return count % ( 10**9 + 7)
                
                    





 
