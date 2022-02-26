# For문에서 순회하는 범위를 줄이는 것이 중요
# 에라토스테네스의 체와 비슷

import sys

MIN, MAX = map(int, sys.stdin.readline().strip().split())

numbers = [True for i in range(MIN, MAX+1)]
answer = len(numbers)

for i in range(2, int(MAX ** 0.5)+1):
    start = MIN // (i**2)
    if MIN % (i**2) != 0:
        start += 1

    for j in range(start*(i*i), MAX+1, i*i):
        if numbers[j-MIN]:
            numbers[j-MIN] = False
            answer -= 1

sys.stdout.write(str(answer))