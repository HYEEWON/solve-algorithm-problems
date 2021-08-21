answer = 0
def dfs(cnt, ret, n, numbers, target):
    global answer
    if cnt == n:
        if ret == target:
            answer += 1
        return

    dfs(cnt+1, ret-numbers[cnt], n, numbers, target)
    dfs(cnt+1, ret+numbers[cnt], n, numbers, target)

def solution(numbers, target):
    dfs(0, 0, len(numbers), numbers, target)
    return answer

print(solution([1, 1, 1, 1, 1], 3))