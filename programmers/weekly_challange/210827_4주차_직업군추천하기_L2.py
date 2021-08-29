from collections import defaultdict

## 개선
def solution(table, languages, preference):
    score = defaultdict(int)

    for t in table:
        t = t.split()
        for lang, pref in zip(languages, preference):
            if lang in t:
                score[t[0]] += pref * (6 - t.index(lang))

    return sorted(score.items(), key=lambda x: (-x[1], x[0]))[0][0]

## 최초 풀이

def solution2(table, languages, preference):
    answer = ''
    language = dict()
    for i in range(len(languages)):
        language[languages[i]] = preference[i]
    
    score = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
    table = sorted(table, key=lambda x : x[0])

    max_cnt = 0
    for t in table:
        t = t.split()
        tmp_cnt = 0
        for i in range(1, 6, 1):
            if t[i] in language.keys():
                tmp_cnt += (language[t[i]] * score[i])

        if tmp_cnt > max_cnt:
            max_cnt = tmp_cnt
            answer = t[0]

    return answer


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
["PYTHON", "C++", "SQL"], [7, 5, 5]))

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
["JAVA", "JAVASCRIPT"], [7, 5]))