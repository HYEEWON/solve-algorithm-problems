# Simulation

def is_balance(p):
    cnt = 0

    for m in p:
        if m == '(':
            cnt += 1
        else:
            cnt -= 1

    return True if cnt == 0 else False


def is_correct(p):
    cnt = 0

    for m in p:
        if m == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False

    return True


def solution(p):  # p: 균형잡힌 괄호 문자열, 짝수 길이
    answer = ''
    if len(p) == 0 or is_correct(p):
        return p

    for c in range(2, len(p) + 1, 2):
        u = p[0:c]
        v = p[c:]
        if not is_balance(u):
            continue
        if is_correct(u):
            return u + solution(v)
        else:
            answer = '(' + solution(v) + ')'

            for i in u[1:-1]:
                if i == '(':
                    answer += ')'
                else:
                    answer += '('

            return answer


## 참고 풀이

def solution(p):
    if p == '': return p

    result, cnt = True, 0
    for i in range(len(p)):
        if p[i] == '(': cnt += 1
        else: cnt -= 1
        if cnt < 0: result = False
        if cnt == 0: # 균형잡힌 문자열이면
            if result: # 올바른 문자열이면
                return p[:i+1] + solution(p[i+1:])
            else:
                return '(' + solution(p[i+1:]) + ')' + ''.join(['(' if x == ')' else ')' for x in p[1:i]])
