n, m = map(int, input().split())
graph_dic = {}

for i in range(1, n+1):
    graph_dic[i] = 0

ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    if  graph_dic[max(a,b)] == 1:
        graph_dic[max(a,b)] = 2
        ans -= 1
    elif graph_dic[max(a,b)] == 0:
        graph_dic[max(a,b)] = 1
        ans += 1


print(ans)
