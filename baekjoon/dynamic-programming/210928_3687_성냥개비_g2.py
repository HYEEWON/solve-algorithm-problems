import sys

# 키: 획 수, 값: 수
numbers = {2: [1], 3: [7], 4: [4], 5: [5, 3, 2], 6: [9, 6, 0], 7: [8]}

T = int(sys.stdin.readline())

max_dp = [0 for i in range(101)]
min_dp = [sys.maxsize for i in range(101)]
min_dp[0] = min_dp[1] = 0

for i in range(2, 8):
    max_dp[i] = numbers[i][0]
    if numbers[i][-1] != 0:
        min_dp[i] = numbers[i][-1]
    else:
        min_dp[i] = numbers[i][-2]

for i in range(4, 101):
    for j in range(2, 8):
        max_dp[i] = max(max_dp[i], int(str(max_dp[i-j])+str(numbers[j][0])))

for i in range(8, 101):
    for j in range(2, 8):
        if not (i-j) in [0, 1]:
            min_dp[i] = min(min_dp[i], int(str(min_dp[i - j])+str(numbers[j][-1])))

for t in range(T):
    N = int(sys.stdin.readline())
    sys.stdout.write(str(min_dp[N]) + " " + str(max_dp[N]) + "\n")