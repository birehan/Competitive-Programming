class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum([n for n in nums if n%2 == 0])
        
        answer = []
        for val, index in queries:
            cur = nums[index] + val
            if cur%2==0:
                if nums[index]%2 != 0: even_sum += cur
                else: even_sum += val

            elif nums[index]%2 == 0:
                even_sum -= nums[index]

            nums[index] += val
            answer.append(even_sum)
    
        return answer


    