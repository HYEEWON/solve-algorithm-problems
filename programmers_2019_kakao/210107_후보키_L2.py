from collections import Counter, defaultdict
from itertools import combinations

def solution(relation):
    answer = 0
    clist = [i for i in range(len(relation[0]))]
    result = []
    for i in range(1, len(relation[0])+1): # 키의 개수
        com = list(combinations(clist, i))
        for c in com:
            d = defaultdict(int)
            for idx in range(len(relation)):
                key = ''
                for cc in c:
                    key += relation[idx][cc]
                d[key] += 1
            if len(d.keys()) == len(relation):
                flag = False
                for r in result:
                    if len(r - set(c)) == 0:
                        flag = True
                        break
                if flag == False:
                    answer += 1
                    result.append(set(c))
    return answer

def solution2(relation):
    answer = 0
    clist = [i for i in range(len(relation[0]))]
    result = []
    for i in range(1, len(relation[0])+1): # 키의 개수
        combination = list(combinations(clist, i))
        for c in combination[:]:
            for r in result:
                if len(r - set(c)) == 0:
                    combination.remove(c)
                    break
        for c in combination:
            d = defaultdict(int)
            for idx in range(len(relation)):
                key = ''
                for cc in c:
                    key += relation[idx][cc]
                d[key] += 1
            if len(d.keys()) == len(relation):
                answer += 1
                result.append(set(c))
    return answer

#(*) 비트 연산
def solution3(relation):
    result = list()
    print(1 << len(relation[0]))
    for i in range(1, 1 << len(relation[0])):
        print(i)
    return result
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution3(relation))