import sys

## 앞에서 부터 접근

T, P = [0], [0]

N = int(sys.stdin.readline())
dp = [0 for i in range(N+1)]

for i in range(N):
    t, p = map(int, sys.stdin.readline().strip().split())
    T.append(t)
    P.append(p)

for i in range(1, N+1):
    if T[i] + i <= N+1:
        dp[T[i] + i-1] = max(dp[T[i] + i-1], P[i] + dp[i-1])
    dp[i] = max(dp[i], dp[i-1])
    print(dp, i)
sys.stdout.write(str(dp[N]))

## 참고한 풀이
# 뒤에서 부터 접근

T, P = [0], [0]

N = int(sys.stdin.readline())
dp = [0 for i in range(N + 2)]

for i in range(N):
    t, p = map(int, sys.stdin.readline().strip().split())
    T.append(t)
    P.append(p)

for i in range(N, 0, -1):

    if T[i] + i <= N + 1:
        dp[i] = max(dp[i + T[i]] + P[i], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

sys.stdout.write(str(dp[1]))