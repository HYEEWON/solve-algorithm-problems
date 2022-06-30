# 최대 공약수

def gcd(w, h):
    max_wh, min_wh = max(w, h), min(w, h)

    while min_wh != 0:
        tmp = max_wh % min_wh
        max_wh = min_wh
        min_wh = tmp
    return max_wh


def solution(w, h):
    return w * h - (w + h - gcd(w, h))