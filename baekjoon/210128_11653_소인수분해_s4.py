#소인수 분해: 소수들의 곱으로 나타낸 것

N = int(input())

i = 2
while N > 1:
    if N % i == 0:
        print(i)
        N //= i 
        continue
    i += 1