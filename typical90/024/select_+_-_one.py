from ssl import ALERT_DESCRIPTION_CLOSE_NOTIFY

from numpy import diff


n, k = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

diff_sum = 0

for a, b in zip(a_list, b_list):
    diff_sum += abs(a-b)

if diff_sum <= k and k%2 == diff_sum%2:
    print('Yes')
else: print('No')
