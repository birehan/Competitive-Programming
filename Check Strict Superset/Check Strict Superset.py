# Enter your code here. Read input from STDIN. Print output to STDOUT
super_set = set(map(int, input().split()))
sub_set_length = int(input())

is_strict = True
for _ in range(sub_set_length):
    sub_set = set(map(int, input().split()))
    
    if not super_set.intersection(sub_set) == sub_set:
        is_strict = False
        break
    if not super_set.difference(sub_set):
        is_strict = False
        break

print(is_strict)
            
