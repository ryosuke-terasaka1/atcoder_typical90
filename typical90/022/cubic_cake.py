a, b, c = map(int, input().split())

def euclid(x, y):
    if min([x, y]) == 0 or x == y:
        return max([x, y])
    else:
        if x < y:
            y = y % x
        else:
            x = x % y
        return euclid(x, y)

r = euclid(a, euclid(b, c))

print((a//r) + (b//r) + (c//r) - 3)
