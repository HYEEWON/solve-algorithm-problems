def solution(s):
    answer = []
    n = [False for i in range(100000)]
    n[0] = True

    s = s[2:-2].split('},{')

    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(',')))
    s = sorted(s, key=lambda x: len(x))

    for arr in s:
        for e in arr:
            if not n[e]:
                answer.append(e)
                n[e] = True

    return answer
