n = int(input())

name_set = set()

for i in range(1, n+1):
    s = input()
    if not s in name_set:
        print(i)
        name_set.add(s)
