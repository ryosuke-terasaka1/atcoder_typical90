def octal_to_decimal(num: int):
    str_num = str(num)
    length = len(str_num)
    result = 0
    for i in range(length):
        result += int(str_num[i]) * (8**(length-1-i))
    return result

def decimal_to_biquinary_notation(num: int):
    p = num
    q = num 
    result = ''
    while p >= 1:
        q = p % 9
        p //= 9
        if q == 8:
            result = '5' + result
        else:
            result = str(q) + result
    return int(result)

n, k = map(int, input().split())
if n > 0: 
    for _ in range(k):
        n = decimal_to_biquinary_notation(octal_to_decimal(n))
print(n)


        

        