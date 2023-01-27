def helper(nums, k):
    nums.sort()
    if k == 0:
        return -1 if nums[0] == 1 else 1
    if k < len(nums) and nums[k-1] == nums[k]:
        return -1
    return nums[k-1]

size = list(map(int, input().split()))
nums = list(map(int, input().split()))

print(helper(nums, size[1]))
