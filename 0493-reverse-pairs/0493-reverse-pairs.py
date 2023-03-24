class Solution:
    def merge(self, left, right):
        merged = []
        jth = right[0] * 2
        index_1, index_2 = 0, 0

        for i in range(len(left)):
            cur = bisect_left(right, (left[i]+1)//2)
            self.count += cur


        while index_1 < len(left) and index_2 < len(right):
            
            if left[index_1] < right[index_2]:
                merged.append(left[index_1])
                index_1 += 1
            else:
                merged.append(right[index_2])
                index_2 += 1
        
        merged.extend(left[index_1:] or right[index_2:])
        return merged

    def conquer(self, left, right, nums):
        if right - left == 1:
            return [nums[left]]

        mid = (left + right)//2
        left_a = self.conquer(left, mid, nums)
        right_a = self.conquer(mid, right, nums)

        return self.merge(left_a, right_a)   


    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0

        self.conquer(0, len(nums), nums)

        return self.count

