length = int(input())
def helper(nums):
    nums.sort()
    for i in range(len(nums)-1, 0, -1):
        if abs(nums[i]-nums[i-1] ) > 1:
            return "NO"
    
    return "YES"

for _ in range(length):
    n = int(input())
    nums = list(map(int, input().split()))
    print(helper(nums))
