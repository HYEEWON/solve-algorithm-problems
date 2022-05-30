def calc_n(n, k):
    answer = ''
    while k >= n:
        answer += str(k % n)
        k = k // n
    answer += str(k)
    return answer[::-1]

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: 
            return False
    return True

def solution(n, k):
    answer = 0
    new_n = calc_n(k, n)

    for num in new_n.split('0'):
        if num.isdigit():
            if is_prime(int(num)):
                answer += 1

    return answer