class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:

        def helper(dic, arr):
            res = [0] * len(arr)
            for index, value in enumerate(arr):
                if value in dic:
                    count, pre_index = dic[value]
                    res[index] = res[pre_index] + count * (index-pre_index)
                    dic[value] = [count+1, index]
                else:
                    dic[value] = [1, index]
            return res
            
        res_forward = helper({}, arr)
        res_backward = reversed(helper({}, arr[::-1]))
        answer = [x + y for x, y in zip(res_forward, res_backward)]
        return answer



      