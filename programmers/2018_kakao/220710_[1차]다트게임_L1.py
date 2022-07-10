# Math, Simulation, regex

import math, re

def solution(dartResult):
    scores, nums, prizes, i = [], [], [], 0

    while i < len(dartResult):
        n = ''
        for i in range(i, i+2):
            if dartResult[i].isdigit():
                n += dartResult[i]
                i += 1
        scores.append(int(n)); nums.append(dartResult[i])

        i += 1
        scores[-1] = math.pow(scores[-1], 1) if nums[-1] == 'S' else math.pow(scores[-1], 2) if nums[-1] == 'D' else math.pow(scores[-1], 3)
        if not i < len(dartResult) or dartResult[i].isdigit():
            prizes.append('')
        else:
            prizes.append(dartResult[i])
            i += 1
            if prizes[-1] == '#':
                scores[-1] *= (-1)
            else:
                scores[-1] *= 2
                if len(scores) > 1:
                    scores[-2] *= 2
    return int(sum(scores))


# 참고 풀이

def solution2(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)

    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)