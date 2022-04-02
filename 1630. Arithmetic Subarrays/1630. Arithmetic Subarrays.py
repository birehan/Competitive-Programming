class Solution(object):

    def checkArithmeticSubarrays(self, nums, l, r):
        def isArithemetic(list):
            if len(list) <= 2:
                return True
            else:
                list.sort()
                for i in range(len(list)-2):
                    if list[i+1]-list[i] != list[i+2]-list[i+1]:
                        return False
                return True
        result = []
        for i in range(len(l)):
            sub_list = nums[l[i]: r[i]+1]
            result.append(isArithemetic(sub_list))
        return result


