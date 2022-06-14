T = int(input())
for t in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[-1]
    money = 0
    for i in range(N - 2, -1, -1):
        if max_price > price[i]:
            money += max_price - price[i]
        else:
            max_price = price[i]
    print('#' + str(t) + ' ' + str(money))