def is_correct_parenthese(parenthese_word: str):
    parenthes_pop_list = []
    for word in parenthese_word:
        if word == '(':
            parenthes_pop_list.append(')')
        else:
            if parenthes_pop_list != []:
                parenthes_pop_list.pop()
            else:
                return False
    
    if not parenthes_pop_list:
        return True
    else:
        return False


import sys
n = int(input())
if n % 2 == 1:
    print('')
    sys.exit()

for i in range(2**n):
    bin_num = format(i, 'b')
    bin_num = list('0'*(n-len(bin_num)) + bin_num)
    if sum(map(int, bin_num)) == n // 2:

        for i in range(n):
            if bin_num[i] == '0':
                bin_num[i] = '('
            else:
                bin_num[i] = ')'
        if is_correct_parenthese(bin_num):
            print("".join(bin_num))







