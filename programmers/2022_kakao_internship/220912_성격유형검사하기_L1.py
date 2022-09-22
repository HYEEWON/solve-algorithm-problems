# 구현, hash table

def solution(survey, choices):
    answer = ''
    number = {'R': 1, 'T': 1, 'C': 2, 'F': 2, 'J': 3, 'M': 3, 'A': 4, 'N': 4}
    score_result = {1: {'R': 0, 'T': 0}, 2: {'C': 0, 'F': 0},
             3: {'J': 0, 'M': 0}, 4: {'A': 0, 'N': 0}}
    score = {1:3, 2:2, 3:1, 4: 0, 5: 1, 6: 2, 7:3}

    for s, c in zip(survey, choices):
        not_agree, agree = list(s)
        if c == 4:
            continue
        elif c <= 3:
            score_result[number[not_agree]][not_agree] += score[c]
        else:
            score_result[number[agree]][agree] += score[c]

    for key in range(1, 5):
        answer += sorted(score_result[key].items(), key=lambda x: (-x[1], x[0]))[0][0]
    return answer