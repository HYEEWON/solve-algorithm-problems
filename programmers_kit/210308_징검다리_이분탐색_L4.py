def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2 # 거리의 최솟값
        minDist = float('inf')
        current, removeCnt = 0, 0

        for rock in rocks:
            diff = rock - current
            if diff < mid:
                removeCnt += 1
            else:
                current = rock
                minDist = min(minDist, diff)
        if removeCnt > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = minDist
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))