class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dfs(index1, index2):
            if index1 >= len(nums1) or index2 >= len(nums2):
                return 0

            if nums1[index1] == nums2[index2]:
                return 1 + dfs(index1+1, index2+1)
            else:
                return max(dfs(index1+1, index2), dfs(index1, index2+1)) 
        
        return dfs(0, 0)