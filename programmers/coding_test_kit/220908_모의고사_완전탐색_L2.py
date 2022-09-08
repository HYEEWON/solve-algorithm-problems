from collections import defaultdict

def solution(answers):
    cnt = defaultdict(int)
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, answer in enumerate(answers):
        cnt[1] = cnt[1]+1 if answer == one[i % len(one)] else cnt[1]
        cnt[2] = cnt[2]+1 if answer == two[i % len(two)] else cnt[2]
        cnt[3] = cnt[3]+1 if answer == three[i % len(three)] else cnt[3]

    cnt = sorted(cnt.items(), key = lambda x: (-x[1], x[0]))
    
    max_val, answer = cnt[0][1], []
    for key, val in cnt:
        if max_val == val:
            answer.append(key)
        else:
            break
    return answer
