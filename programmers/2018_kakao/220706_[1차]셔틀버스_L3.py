# Simulation

from collections import deque

def get_answer(n):
    return '{0:02d}'.format(n // 60) + ':' + '{0:02d}'.format(n % 60)

def solution(n, t, m, timetable):
    answer, last_bus_time = 0, 540 + (n - 1) * t # 시간은 분단위로 계산

    timetable = deque(sorted([int(i[:2])*60+int(i[3:]) for i in timetable]))

    for time in range(540, 540 + (n - 1) * t + 1, t): # time: 버스 출발 시간
        for cnt in range(1, m+1):
            if timetable:
                if timetable[0] > last_bus_time: # 크루가 나오는 시간이 마지막 버스 시간보다 늦는 경우
                    return get_answer(last_bus_time) # 마지막 버스 탑승
                elif timetable[0] <= time: #크루가 나온 시간에 버스를 탈 수 있을 경우
                    if time == last_bus_time and cnt == m: # 마지막 버스이고 1명 더 탈 수 있는 경우
                        return get_answer(timetable[0] - 1) # 크루보다 1분 전에 나와서 탑승
                    timetable.popleft() # 버스 탑승
            else: # 다른 크루가 없다면 마지막 버스 탑승
                return get_answer(last_bus_time)
