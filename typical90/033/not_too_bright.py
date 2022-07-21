h, w = map(int, input().split())

if min(h, w) == 1:
    print(h*w)

else:
    h_max = (h//2) + h%2
    w_max = (w//2) + w%2

    print(h_max * w_max)
