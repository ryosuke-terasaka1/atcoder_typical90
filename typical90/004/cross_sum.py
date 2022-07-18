h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [[0 for _ in range(w)] for _ in range(h)]

h_sum = [sum(a[y][:]) for y in range(h)]
w_sum = [sum([s[x] for s in a]) for x in range(w)]

for y in range(h):
    for x in range(w):
        b[y][x] = h_sum[y] + w_sum[x] - a[y][x]

for sum_list in b:
    print(*sum_list)
