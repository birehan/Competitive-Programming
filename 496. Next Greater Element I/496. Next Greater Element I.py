class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        if len(nums2) == 0:
            return []

        stack = []
        stack.append(nums2.pop(0))
        result = {}
        while len(nums2) != 0:
            cur = nums2.pop(0)
            while len(stack) > 0 and stack[-1] < cur:
                result[stack.pop()] = cur
            stack.append(cur)

        for i in stack:
            result[i] = -1

        answer = []

        for j in nums1:
            answer.append(result[j])

        return answer

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
