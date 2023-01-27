def helper(nums):
    total = 0
    cur = nums[0]
    for i in range(1, len(nums)):
        if (nums[i] > 0 and nums[i-1] > 0) or (nums[i] < 0 and nums[i-1] < 0):
            cur = max(cur, nums[i])
        else:
            total += cur
            cur = nums[i]
    
    total += cur
    return total


length = int(input())
for _ in range(length):
    n = int(input())
    nums = list(map(int, input().split()))
    print(helper(nums))
