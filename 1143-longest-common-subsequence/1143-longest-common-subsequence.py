class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n1, n2 = len(text1), len(text2)     
        bef, aft = [0]*(n2+1), [0]*(n2+1)   
        for i in range(n1):                
            for j in range(n2):            

                if text1[i] == text2[j]:    
                    aft[j+1] = 1 + bef[j] 

                elif aft[j] > bef[j+1]:   
                    aft[j+1] = aft[j]      
                else:                      
                    aft[j+1] = bef[j+1]   

            aft, bef = bef, aft                                                            
        return bef[-1]  