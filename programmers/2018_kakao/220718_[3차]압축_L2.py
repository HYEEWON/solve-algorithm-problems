# Simulation

def solution(msg):
    answer = []
    d = {chr(i): i-64 for i in range(65, 91)}

    maxl, s, next = 1, 0, 27
    while s < len(msg):
        for e in range(s+maxl, s, -1):
            if msg[s:e] in d.keys():
                answer.append(d[msg[s:e]])
                if e < len(msg):
                    d[msg[s:e+1]] = next
                    next += 1
                    maxl += 1
                    break
                else:
                    break
        s = e
    return answer