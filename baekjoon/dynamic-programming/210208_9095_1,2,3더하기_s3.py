
numbers = [1, 2, 3]

T = int(input())
for t in range(T):
    n = int(input())

    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(len(numbers)):
            if (i >= numbers[j]):
                dp[i] += dp[i-numbers[j]] 
                print(i, dp[i-numbers[j]])

    print(dp[n])