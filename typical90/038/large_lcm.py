large_num = 10**18

a, b = map(int, input().split())

def euclid(x, y):
    r = x % y
    while r != 0:
        x, y = y, r
        r = x % y
    return y

r = b // euclid(a, b)

if r > (large_num / a): ans = 'Large'
else:
  ans = int(a * r)
  if ans > large_num:
    ans = 'Large'

print(ans)