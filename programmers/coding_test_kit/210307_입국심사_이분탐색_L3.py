def solution(n, times):
    start, end = 0, max(times) * n
    answer = 0
    while start <= end:
        mid = (start + end) // 2    
        tmp  = sum(mid//t for t in times)

        if tmp >= n:
            end  = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer

print(solution(6, [7, 10]))
print(solution(2, [1, 2]))