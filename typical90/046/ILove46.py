import itertools


n = int(input())
a = [int(x) % 46 for x in input().split()]
b = [int(x) % 46 for x in input().split()]
c = [int(x) % 46 for x in input().split()]

sum_46 = 0
a_n = [0]*46
b_n = [0]*46
c_n = [0]*46

for i in range(n):
    a_n[a[i]] += 1
    b_n[b[i]] += 1
    c_n[c[i]] += 1

for i, j, k in itertools.product(range(46), range(46), range(46)):
    if (i+j+k) % 46 == 0:
        sum_46 += a_n[i] * b_n[j] * c_n[k]

print(sum_46)