e = int(input())
english = set(map(int, input().split()))
f = int(input())
french = set(map(int, input().split()))
only_english = english.union(french)
print(len(only_english))
