class Solution:
    def helper(self, cur, index):
        self.max_len = max(self.max_len, len(cur))

        if index == len(self.arr):
            return
        
        
        if len(Counter(cur + self.arr[index])) == len(cur + self.arr[index]):
            self.helper(cur + self.arr[index], index+1)

        self.helper(cur, index+1)
        
    def maxLength(self, arr: List[str]) -> int:
        self.max_len = 0
        self.arr = arr
        self.helper("", 0)

        return self.max_len