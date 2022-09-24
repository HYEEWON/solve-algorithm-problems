import sys

prime = []
def findPrime(n): # 에라토스테네스의 체
    is_prime = [True for i in range(n)]
    is_prime[0] = is_prime[1] = False

    for i in range(2, n):
        if not is_prime[i]:
            continue
        for k in range(i*2, n, i):
            is_prime[k] = False

    for i in range(2, n):
        if is_prime[i]:
            prime.append(i)

N = int(sys.stdin.readline())
findPrime(N+1)

start = 0
end = 0
answer = 0

while start < len(prime) and end < len(prime):
    tmpSum = sum(prime[start:end+1])
    if tmpSum < N:
        end += 1
    elif tmpSum > N:
        start += 1
    else:
        start += 1
        end += 1
        answer += 1

sys.stdout.write(str(answer))