# math

from itertools import combinations

is_prime = [True for i in range(3000)]
is_prime[1] = False


def solution(nums):
    answer = 0

    for i in range(2, 3000):
        if is_prime[i]:
            for j in range(i * 2, 3000, i):
                is_prime[j] = False

    for c in list(combinations(nums, 3)):
        if is_prime[sum(c)]:
            answer += 1
    return answer