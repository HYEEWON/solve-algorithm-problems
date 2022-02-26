import sys

def isPrime(n):
    arr = [True] * (n+1)
    arr[0] = arr[1] = False
    for i in range(2, n//2+1):
        if arr[i] == True:
            for j in range(i*2, n+1, i):
                arr[j] = False
    return arr

primes = isPrime(1000000)

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    
    flag = True
    for i in range(2, len(primes) // 2+1):
        if primes[i] == True and primes[n-i] == True:
            sys.stdout.write(str(n)+' = '+str(i)+' + '+str(n-i)+'\n')
            flag = False
            break
    if flag == True:
        sys.stdout.write("Goldbach's conjecture is wrong.")