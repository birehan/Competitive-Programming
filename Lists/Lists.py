if __name__ == '__main__':
    store = []
    dic = {
        "insert": lambda x: store.insert(int(x[0]), int(x[1])),
        "remove": lambda x: store.remove(int(x[0])),
        "append": lambda x: store.append(int(x[0])),
        "print": lambda x: print(store),
        "sort": lambda x: store.sort(),
        "pop": lambda x: store.pop(),
        "reverse": lambda x : store.reverse()
    }
    N = int(input())
    for _ in range(N):
        value =input().split()
        inputs = value[1:]
        dic[value[0]](inputs)
