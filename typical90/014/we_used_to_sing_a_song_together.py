from unittest import result


n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort()

result = 0

for a, b in zip(a_list, b_list):
    result += abs(a-b)
    
print(result)
