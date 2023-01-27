def helper(nums):
    find = [False, False]
    for i in nums:
        if i%2 == 0:
            find[0] = True
        else:
            find[1] = True
    
    if not find[0] or not find[1]:
        return nums
    nums.sort()
    return nums
n = int(input())
nums = list(map(int, input().split()))
print(*helper(nums))
