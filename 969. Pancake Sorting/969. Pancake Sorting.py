class Solution(object):
    def pancakeSort(self, arr):
        flip = []

        for i in range(len(arr), 1, -1):
            cur_max = max(arr[:i])

            index_max = arr.index(cur_max)
            flip.append(index_max + 1)
            flip.append(i)
            l, r = 0, index_max
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            le, ri = 0, i - 1

            while le < ri:
                arr[le], arr[ri] = arr[ri], arr[le]
                le += 1
                ri -= 1
        return flip

        """
        :type arr: List[int]
        :rtype: List[int]
        """
