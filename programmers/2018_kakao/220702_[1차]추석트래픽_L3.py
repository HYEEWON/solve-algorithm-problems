# Simulation

import re

# 밀리초 단위로 계산
# 초 단위로 계산하면 부동 소수점 오차 발생

def calc(finish):
    finish = list(map(int, re.split('[:|.]', finish)))
    return (finish[0] * 3600 + finish[1] * 60 + finish[2]) * 1000 + finish[3]

def solution(lines):
    answer = 1
    time_line = []

    for line in lines:
        date, finish, time = line.split()
        time = time[:-1].split('.')

        if len(time) > 1:
            time = int(time[0]) * 1000 + int(time[1])
        else:
            time = int(time[0]) * 1000

        c = calc(finish)
        time_line.append([c - time + 1, c])

    for idx, time in enumerate(time_line):
        cnt = 1
        for i in range(idx + 1, len(time_line)):
            # 앞 함수가 끝나는 시간 + 999 전에 다음 함수가 시작하면 됨
            if time[1] + 999 >= time_line[i][0]:
                cnt += 1
        answer = max(answer, cnt)
    return answer