def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)

    for i in range(len(citations)):
        if citations[i] <= i:
            answer = i
            break
    if i == len(citations):
        return i
    return answer

print(solution([3, 0, 6, 1, 5]))