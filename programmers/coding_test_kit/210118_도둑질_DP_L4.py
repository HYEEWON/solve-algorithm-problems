def solution(money):
    mem1 = [0 for i in range(len(money))]
    mem1[0] = money[0]
    mem1[1] = max(money[0], money[1])
    
    for i in range(2, len(money)-1):
        mem1[i] = max(mem1[i-2]+money[i], mem1[i-1])
    mem1[-1] = mem1[-2]
    
    mem2 = [0 for i in range(len(money))]
    mem2[0] = 0
    mem2[1] = money[1]
    for i in range(2, len(money)):
        mem2[i] = max(mem2[i-2]+money[i], mem2[i-1])
    return max(mem1[-1], mem2[-1])