# Regex, Simulation

import re

def solution(m, musicinfos):
    answer = []
    p = re.compile('([ABCDEFG][#]?)')
    m = p.findall(m)

    for i, musicinfo in enumerate(musicinfos):
        musicinfos[i] = musicinfo.split(',')
        musicinfos[i][0] = int(musicinfos[i][0][:2]) * 60 + int(musicinfos[i][0][3:])
        musicinfos[i][1] = int(musicinfos[i][1][:2]) * 60 + int(musicinfos[i][1][3:])

        music = p.findall(musicinfos[i][3])
        idx, cnt, tmp, len_m = 0, 0, [], len(m)
        while cnt < (musicinfos[i][1] - musicinfos[i][0]):
            if len(tmp) >= len(m) and tmp:
                del tmp[0]
            tmp.append(music[idx])

            cnt += 1
            idx = (idx + 1) % len(music)

            if m == tmp:
                answer.append([musicinfos[i][2], (musicinfos[i][1] - musicinfos[i][0]), i])

    answer = sorted(answer, key=lambda x: (-x[1], x[2]))
    if answer:
        return answer[0][0]
    return '(None)'