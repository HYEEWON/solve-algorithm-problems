import sys

numbers = [0, 1, 2, 3]

T = int(sys.stdin.readline().strip())
for t in range(T):
    n = int(sys.stdin.readline().strip())

    # dp[i][j]: i를 만들 때, 마지막으로 사용할 수 있는 수가 numbers[j-1]
    dp = [[0 for i in range(len(numbers)+1)] for j in range(n+1)]
    dp[0] = [1] * (len(numbers)+1)
    for i in range(1, n+1):
        for j in range(1, len(numbers)+1):
            if (i >= numbers[j-1]):
                dp[i][j] = dp[i][j-1]+dp[i-numbers[j-1]][j]
            else:
                dp[i][j] = dp[i][j-1]
    sys.stdout.write(str(dp[n][len(numbers)-1])+'\n')

###
import sys

numbers = [0, 1, 2, 3]

T = int(sys.stdin.readline().strip())
for t in range(T):
    n = int(sys.stdin.readline().strip())

    dp = [[0 for i in range(len(numbers))] for j in range(n+1)]
    dp[0] = [1] * (len(numbers))
    for i in range(1, n+1):
        for j in range(1, len(numbers)):
            if (i >= numbers[j]):
                dp[i][j] = dp[i][j-1]+dp[i-numbers[j]][j]
            else:
                dp[i][j] = dp[i][j-1]
    sys.stdout.write(str(dp[n][len(numbers)-1])+'\n')