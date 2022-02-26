# 에라토스테네스의 체: N보다 작거나 같은 모든 소수를 찾는 알고리즘

N, K = map(int, input().split())

arr = [True] * (N+1)
arr[0] = arr[1] = False

k = 0
answer = 0
for i in range(2, N+1):
    if arr[i] == True:    
        for j in range(i, N+1, i):
            if arr[j] == True:
                arr[j] = False
                k += 1
                if k == K:
                    answer = j
                    break

print(answer)