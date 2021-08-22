##(*)해설 참조

def time_to_sec(time): # "00:00:00" 형식
    time = time.split(':')
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

def sec_to_time(sec):
    h = sec // 3600
    m = (sec - h*3600) // 60
    s = (sec - h*3600 - m*60)    
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)

def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    
    timeline = [0 for i in range(play_time_sec + 1)]

    # timeline[i]: i 시간에 시작된 재생 구간 수 - i 시간에 종료된 재생 구간 수
    for i in range(len(logs)):
        start, end = logs[i].split('-')
        timeline[time_to_sec(start)] += 1
        timeline[time_to_sec(end)] -= 1
    
    # 현재 시청자 수
    # timeline[i]: i ~ i+1의 구간의 재생 구간 수
    for i in range(1, play_time_sec+1):
        timeline[i] = timeline[i] + timeline[i-1]

    # 누적 시청자 수
    # timeline[i]: 0 ~ i+1까지 누적 재생 시간
    for i in range(1, play_time_sec+1):
        timeline[i] = timeline[i] + timeline[i-1]

    max_time = timeline[adv_time_sec - 1] # 0초에 광고 시작 시, 누적 시간
    min_start_time = 0

    for i in range(adv_time_sec, play_time_sec):
        time = timeline[i] - timeline[i-adv_time_sec]

        if time > max_time:
            max_time = time
            min_start_time = i - adv_time_sec + 1
            # timeline[end] - timeline[start]: start+1 ~ end 사이의 누적 시간

    return sec_to_time(min_start_time)   


## 초기 풀이: 19.4/100
# 시간 초과

def time_to_sec(time): # "00:00:00" 형식
    time = time.split(':')
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

def sec_to_time(sec):
    h = sec // 3600
    m = (sec - h*3600) // 60
    s = (sec - h*3600 - m*60)    
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)

def solution2(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    logs.sort()

    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)

    for i in range(len(logs)):
        log = logs[i].split('-')
        logs[i] = [time_to_sec(log[0]), time_to_sec(log[1])]

    max_time = 0
    min_start_time = 0

    for i in range(len(logs)):
        start_time = logs[i][0]
        end_time = start_time + adv_time_sec
        if end_time > play_time_sec:
            continue
        calc_time = 0
        
        for log in logs:
            if log[1] < start_time or log[0] > end_time:
                pass
            elif log[0] < start_time:
                if log[1] >= end_time:
                    calc_time += adv_time_sec
                else:
                    calc_time += (log[1] - start_time)
            elif log[0] >= start_time:
                if log[1] <= end_time:
                    calc_time += adv_time_sec
                else:
                    calc_time += (end_time - log[0])           
        
        if max_time < calc_time:
            max_time = calc_time
            min_start_time = start_time

    return sec_to_time(min_start_time)

print(solution("02:03:55", 	"00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))