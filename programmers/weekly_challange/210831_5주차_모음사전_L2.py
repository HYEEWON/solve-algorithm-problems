from itertools import product

def solution(word):
    result = []
    for i in range(1, 6):
        for p in product("AEIOU", repeat=i):
            result.append("".join(p))
    result.sort()
    for i in range(len(result)):
        if (word == result[i]):
            return i+1
    return

def solution2(word):
    answer = 0
    diff = 781
    alpha = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    for idx in range(len(word)):
         answer += (alpha[word[idx]] * diff) + 1
         diff = (diff - 1) // 5
    return answer

print(solution("AAAE"))