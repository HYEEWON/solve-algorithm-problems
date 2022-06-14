# 구현

# 등수 계산
# 배열 이용 가능, set으로 & 연산으로 가능
def get_grade(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    max_v, min_v = 0, 0

    for n in lottos:
        if n == 0:
            max_v += 1
        elif n in win_nums:
            max_v += 1
            min_v += 1

    return [get_grade(max_v), get_grade(min_v)]