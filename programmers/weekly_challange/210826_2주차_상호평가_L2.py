def get_grade(n):
    if n >= 90:
        return 'A'
    elif 90 > n >= 80:
        return 'B'
    elif 80 > n >= 70:
        return 'C'
    elif 70 > n >= 50:
        return 'D'
    else:
        return 'F'

def get_score(idx, n, scores):
    score = []
    for i in range(n):
        score.append(scores[i][idx])
    return score

def solution(scores):
    answer = ''
    n = len(scores)

    for i in range(n):
        score = get_score(i, n, scores)
        max_score = max(score)
        min_score = min(score)
        avg_score = 0
        #print(i, score, max_score, " ###############")
        if score.count(max_score) == 1 and score.index(max_score) == i:
            total_sum = sum(score) - max_score
            avg_score = total_sum / (len(score)-1)
            #print(total_sum, avg_score, " if")
        elif score.count(min_score) == 1 and score.index(min_score) == i:
            total_sum = sum(score) - min_score
            avg_score = total_sum / (len(score)-1)
            #print(total_sum, avg_score, " if 2")
        else:
            total_sum = sum(score)
            avg_score = total_sum / len(score)
            #print(total_sum, avg_score, " else 3")

        answer += get_grade(avg_score)
    return answer


print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))