import sys

'''
    ax + by + e = 0
    cx + dy + f = 0
    
    x = (bf - ed) / (ad - bc)
    y = (ec - af) / (ad - bc)
'''


def is_int(x):
    if x == int(x):
        return True
    else:
        return False


def solution(line):
    top, bottom, left, right = -sys.maxsize, sys.maxsize, sys.maxsize, -sys.maxsize
    points = []

    for i in range(0, len(line) - 1):
        for j in range(1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]

            # 평행 또는 일치
            if a * d - b * c == 0:
                continue

            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if is_int(x) and is_int(y):
                top, bottom = int(max(top, y)), int(min(bottom, y))
                left, right = int(min(left, x)), int(max(right, x))
                points.append((int(x), int(y)))

    answer = [['.' for i in range(right - left + 1)] for j in range(top - bottom + 1)]

    for point in points:
        answer[top - point[1]][point[0] - left] = '*'

    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    return answer
