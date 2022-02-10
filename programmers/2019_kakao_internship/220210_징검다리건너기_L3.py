# 이분탐색
# 답의 범위: 0 ~ 200000000 -> 이분탐색 진행
import copy


def check(stones, k, n):
    skip = 0

    tmp_stones = copy.deepcopy(stones)
    for stone in tmp_stones:
        if stone - n < 0:
            skip += 1
        else:
            skip = 0

        if skip >= k:
            return False

    return True


def solution(stones, k):
    answer = 0
    start, end = 0, 200000000

    while start <= end:
        mid = (start + end) // 2

        if check(stones, k, mid):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer
