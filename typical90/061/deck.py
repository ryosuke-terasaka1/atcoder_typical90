q = int(input())
y = []

for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        y.insert(0, x)
    elif t == 2:
        y.append(x)
        
    else: print(y[x-1])
