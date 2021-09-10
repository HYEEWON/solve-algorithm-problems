from collections import defaultdict

## 통과한 풀이
# 딕셔너리를 사용해 보석 종류의 개수를 Counting

def solution(gems):
    answer = [1, len(gems)]
    total_gem_cnt = len(set(gems))
    left, right = 0, 0

    gem_dict = defaultdict(int)
    gem_dict[gems[0]] += 1

    while True:
        if left > right or right >= len(gems):
            break
        if len(gem_dict.keys()) >= total_gem_cnt:
            if answer[1] - answer[0] > right - left:
                answer = [left+1, right+1]
            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]
            left += 1
        else:
            right += 1
            if right >= len(gems):
                break
            gem_dict[gems[right]] += 1
    return answer


## 42.2 / 100.0
# 정확성은 모두 통과, 효율성에서 일부 실패

def solution(gems):
    answer = [1, len(gems)]
    total_gem_cnt = len(set(gems))
    left, right = 0, 0

    while True:
        if left > right or right >= len(gems):
            break
        tmp_gem_cnt = len(set(gems[left:right+1]))
        if tmp_gem_cnt >= total_gem_cnt:
            if answer[1] - answer[0] > right - left:
                answer = [left+1, right+1]
            left += 1
        else:
            right += 1
    return answer