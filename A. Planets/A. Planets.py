from collections import Counter
def helper(orbits, second_machine):
    cost = 0
    orbit_count = Counter(orbits)
    for value in orbit_count.values():
        cost += min(value, second_machine)
    return cost

length = int(input())

for _ in range(length):
    value = list(map(int, input().split()))
    orbits = list(map(int, input().split()))
    print(helper(orbits, value[1]))

