# Math

alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def n_num(num, n):
    res = ''
    if num == 0:
        return str(num)
    while num > 0:
        tmp = num%n if num%n < 10 else alpha[num%n]
        res = str(tmp) + res
        num //= n
    return res

def solution(n, t, m, p):
    answer, tmp = '', ''
    num = 0
    while len(tmp) <= m*t:
        tmp += n_num(num, n)
        num += 1
    for i in range(p-1, len(tmp), m):
        answer += tmp[i]
        if len(answer) == t:
            break
    return answer