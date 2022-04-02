def dominoPilling(M, N):
    if M * N < 2:
        return 0
    else:
        return (M * N) // 2


(a, b) = map(int, input().split())
print(dominoPilling(a, b))