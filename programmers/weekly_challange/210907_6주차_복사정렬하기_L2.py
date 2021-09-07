def solution(weights, head2head):
    answer = []
    people = []

    for idx, (w, h) in enumerate(zip(weights, head2head)):
        h = list(h)
        if h.count("N") == len(h):
            win_rate = 0
        else:
            win_rate = list(h).count("W") / (list(h).count("W")+list(h).count("L"))
        win_cnt = 0
        for i in range(len(weights)):
            if h[i] == 'W' and w < weights[i]:
                win_cnt += 1
        people.append((win_rate, win_cnt, w, idx+1))

    people = sorted(people, key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    for p in people:
        answer.append(p[3])

    return answer

print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))