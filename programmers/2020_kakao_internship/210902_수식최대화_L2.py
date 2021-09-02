import re
from itertools import permutations

## 사용한 풀이
def calculation(n1, n2, op):
    if op == '-':
        return n1 - n2
    elif op == '+':
        return n1 + n2
    else:
        return n1 * n2

def solution(expression):
    answer = 0
    number = re.split('-|\+|\*', expression)
    operation = []
    for e in expression:
        if e in ['-', '+', '*']:
            operation.append(e)

    ranks = list(permutations(set(operation), len(set(operation))))
    print(ranks)

    for rank in ranks:
        numbers = number.copy()
        operations = operation.copy()
        for op in rank:
            while op in operations:
                idx = operations.index(op)
                tmp = calculation(int(numbers[idx]), int(numbers[idx + 1]), op)
                numbers.pop(idx + 1)
                numbers.pop(idx)
                operations.pop(idx)
                numbers.insert(idx, tmp)

        answer = max(abs(numbers[0]), answer)
    return answer


## 참고할 풀이
## 출처: 프로그래머스 다른 사람 풀이

def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        print(a, b)
        temp_list = []
        for e in expression.split(a):
            print(e)
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
            print(temp, temp_list)
        answer.append(abs(eval(a.join(temp_list))))
        print(a.join(temp_list))
    return max(answer)

print(solution("100-200*300-500+20"))