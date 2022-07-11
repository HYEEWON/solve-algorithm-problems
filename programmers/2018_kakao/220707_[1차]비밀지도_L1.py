# Simulation, String

# 참고 (rjust(), ljust())
## "a".rjust(5): '    a'
## "a".rjust(5, '.'): '....a'

def get_10_n(size, n):
    ans = ''
    while n >= 1:
        ans = str(n%2) + ans
        n //= 2
    return list(('{0:0'+str(size)+'d}').format(int(ans)))

def solution(n, arr1, arr2):
    answer = []
    for a in arr1:
        answer.append(get_10_n(n, a))
    
    for y, a in enumerate(arr2):
        for x, b in enumerate(get_10_n(n, a)):
            answer[y][x] = '#' if answer[y][x] == '1' or b == '1' else ' '
        answer[y] = ''.join(answer[y])
    return answer
