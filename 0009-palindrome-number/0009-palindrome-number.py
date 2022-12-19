class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        c = deepcopy(x)
        rev = 0
        while c:
            rev = rev* 10 + c%10
            c = c//10

        return rev == x  