global count


def merge(left, right):
    global count
    if right[0] -left[-1] == 1:
        return left + right

    if left[0] - right[-1] == 1:
        count += 1
        return right + left
    
    return [-1]

def conquer(nums, left, right):
    if right - left == 1:
        return [nums[left]]
    
    mid = (left + right)//2

    left_a = conquer(nums, left, mid)
    right_a = conquer(nums, mid, right)
    

    merged = merge(left_a, right_a)
    if merged == [-1] or left_a == [-1] or right_a == [-1]:
        return [-1]

    return merged


length = int(input())

for _ in range(length):
    count = 0

    n = int(input())
    nums = list(map(int, input().split()))
    res = conquer(nums, 0, len(nums))
    if res == [-1]:
        print(-1)
    else:
        print(count)
    

    
