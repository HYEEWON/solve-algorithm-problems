import re

def multi(arr):
    return eval('*'.join([str(n) for n in arr]))

def solution(user_id, banned_id):
    answer = 0
    patterns = ['' for i in range(len(banned_id))]
    cnt = [0 for i in range(len(banned_id))]

    for idx in range(len(banned_id)):
        ban = banned_id[idx].split('*')
        pattern = '^'
        for i in range(len(ban)):
            if ban[i] == '':
                pattern += '.'
            else:
                pattern += ban[i]
                if i != len(ban)-1 and ban[i+1] != '':
                    pattern += '.'
        patterns[idx] = pattern + '$'
    #print(patterns)
    for i in range(len(patterns)):
        pattern = re.compile(patterns[i])
        for id in user_id:
            #print(pattern.match(id), id)
            if pattern.match(id) != None:
                cnt[i] += 1
    #print(cnt)

    return multi(cnt)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))