n = int(input())
a,b,c = map(int, input().split())

ans = 10000

a_max_num = n // a + 1

for i in range(a_max_num):
    for j in range(10000-i):
        if n >= a*i + b*j:
            k = (n-(a*i+b*j)) // c
            if (n-(a*i+b*j)) % c == 0 and i+j+k <= 9999:
                ans = min(ans, i+j+k)
            
print(ans)
