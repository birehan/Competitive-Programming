class Solution:
    def conquer(self, left, right, diff):
        p2 = 0
        for p1 in range(len(left)):
            self.count += len(right) - bisect_left(right, left[p1]- diff)
        merged = []
        p1 = p2 = 0
        while p1 < len(left) and p2 < len(right):
            if left[p1] < right[p2]:
                merged.append(left[p1])
                p1 += 1
            else:
                merged.append(right[p2])
                p2 += 1
            
        merged.extend(left[p1:] or right[p2:])
        return merged
    
    def divide(self, left, right, nums1, diff):
        if left + 1 == right:
            return [nums1[left]]

        mid = (left + right)//2
        left_a = self.divide(left, mid, nums1, diff)
        right_a = self.divide(mid, right, nums1, diff)

        return self.conquer(left_a, right_a, diff)

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]

        self.count = 0
        self.divide(0, len(nums1), nums1, diff)

        return self.count


