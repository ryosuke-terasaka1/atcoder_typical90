n = int(input())

class_1_sum = [0 for _ in range(n+1)]
class_2_sum = [0 for _ in range(n+1)]

for i in range(1, n+1):
    c, p = map(int, input().split())
    if c == 1:
        class_1_sum[i] = class_1_sum[i-1] + p
        class_2_sum[i] = class_2_sum[i-1]
    if c == 2:
        class_1_sum[i] = class_1_sum[i-1]
        class_2_sum[i] = class_2_sum[i-1] + p

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    a, b = class_1_sum[r]-class_1_sum[l-1], class_2_sum[r]-class_2_sum[l-1]
    print(a, b)
