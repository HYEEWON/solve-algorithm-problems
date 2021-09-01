def solution(price, money, count):
    total_price = 0
    for c in range(1, count+1):
        total_price += price * c

    if total_price > money:
        return total_price - money
    else:
        return 0