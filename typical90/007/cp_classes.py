n = int(input())

a = list(map(int, input().split()))

a.sort()
a_length = len(a)
a_middle_length = a_length // 2


q = int(input())

for _ in range(q):
    b = int(input())
    left, right = 0, a_length-1
    while right - left > 1:
        middle = ((left + right) // 2 + (left + right) % 2)
        # print(left, right)
        if a[middle] == b:
            left, right = middle, middle
        elif a[middle] < b:
            left = middle
        else:
            right = middle
    print(min(abs(b-a[left]), abs(b-a[right])))


