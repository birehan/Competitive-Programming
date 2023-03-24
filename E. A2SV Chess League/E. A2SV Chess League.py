length, min_dif = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
indexs = [i for i in range(len(nums))]

def merge(left, right, min_dif):
    merged = []
    index_1, index_2 = 0, 0

    while index_1 < len(left) and index_2 < len(right):
        if nums[left[index_1]] < nums[right[index_2]]:
            if nums[right[index_2]] - nums[left[index_1]] <= min_dif:
                merged.append(left[index_1])
            
            index_1 += 1
        
        else:
            if nums[left[index_1] ] - nums[right[index_2]] <= min_dif:
                merged.append(right[index_2])
            
            index_2 += 1
        
    merged.extend(left[index_1:] or right[index_2:])
    return merged


def conquer(left, right):
    if right - left == 1:
        return [left]

    mid = (left + right)//2
    left_a = conquer(left, mid)
    right_a = conquer(mid, right)
    merged = merge(left_a, right_a,min_dif)
    
    return merged

res = (conquer(0, len(nums)))
res = [i+1 for i in res]
res.sort()

print(*res)
        
