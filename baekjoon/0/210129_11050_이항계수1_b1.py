import math

def multi(n):
    if n == 0 or n == 1: return 1
    else: return n*multi(n-1)
    
n, k = map(int, input().split())
ans = multi(n) / (multi(k)*multi(n-k))
print(int(ans))