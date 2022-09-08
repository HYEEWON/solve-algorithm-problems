import math

def solution(brown, yellow):
    answer = []
    number = get_divisor(yellow)
    
    for n1, n2 in number:
        cnt = n1*2 + n2*2 + 4
        if cnt == brown:
            return [n1+2, n2+2]
    
def get_divisor(yellow): # 약수 찾기
    number = []
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            number.append(sorted([i, yellow // i], key=lambda x: -x))
    return number
