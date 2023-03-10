class Solution:
    def helper(self, values, index):
        if index == len(self.cookies):
            self.min_dif = min(max(values), self.min_dif)
            return  
        
        if self.min_dif <= max(values):
            return
    
        for i in range(len(values)):
            values[i] +=self.cookies[index]
            self.helper(values, index+1)
            values[i] -= self.cookies[index]

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        self.min_dif = inf
        self.cookies = cookies
        self.helper([0]*k, 0)

        return self.min_dif