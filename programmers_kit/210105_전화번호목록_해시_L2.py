def solution(phone_book):
    answer = True
    n = len(phone_book)
    for i in range(n):
        for j in range(n):
            if i != j and phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return answer

def solution2(phone_book):
    phone_book = sorted(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

# 해시를 이용한 풀이
def solution3(phone_book):
    n = len(phone_book)
    d = dict()
    for i in range(n):
        d[phone_book[i]] = 1

    for i in range(n):
        tmp = ''
        for t in phone_book[i]:
            tmp += t
            if tmp in d and tmp != phone_book[i]:
                return False
    return True

phone_book = ['119', '97674223', '1195524421']
solution2(phone_book)