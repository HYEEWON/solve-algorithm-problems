from math import gcd

up = []
down = []

for i in range(2):
    a, b = map(int, input().split())
    up.append(a)
    down.append(b)

fraction = [up[0]*down[1]+up[1]*down[0], down[0]*down[1]]

gcds = gcd(fraction[0], fraction[1])
fraction[0], fraction[1] = fraction[0]//gcds, fraction[1]//gcds
print(fraction[0], fraction[1])