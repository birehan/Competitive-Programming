class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(string):
            return string[::-1]
            
        def invert(string):
            return ''.join(['1'if i == '0' else '0' for i in string])
          
        def find(n, dic):
            if n-1 not in dic:
                dic[n-1] = find(n-1, dic)
            return dic[n-1] + "1" + reverse(invert(dic[n-1]))
        
        dic = {0:'0'}
        res = find(n, dic)
        
        return res[k-1]
