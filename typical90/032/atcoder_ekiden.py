import itertools


n = int(input())

a = []

ans = 10000

for _ in range(n):
    a.append(list(map(int, input().split())))

m = int(input())

b = []

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    b.append(set([x, y]))
    
for v in itertools.permutations(range(n), n):
    tmp_ans = 0
    for i in range(n):
        tmp_ans += a[v[i]][i]
        if i >= 1:
            if set([v[i-1], v[i]]) in b:
                tmp_ans = 10000
                break
    ans = min(tmp_ans, ans)

if ans == 10000:
    ans = -1

print(ans)
        

