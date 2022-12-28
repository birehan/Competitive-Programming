def helper(size1, size2):
    dic = {("S", "M"): "<", ("S", "L"): "<", ("M", "M"): "=",
           ("M", "S"): ">", ("M", "L"): "<", ("L", "M"): ">",
           ("L", "S"): ">"
           }
    if size1 == size2:
        return "="
    if size1[-1] == "S" and size2[-1]=="S":
        return ">" if len(size1) < len(size2) else "<"

    elif size1[-1] == "L" and size2[-1] == "L":
        return ">" if len(size1) > len(size2) else "<"

    return dic[(size1[-1], size2[-1])]

n = int(input())

for _ in range(n):
    sizes = input().split()
    print(helper(sizes[0], sizes[1]))
