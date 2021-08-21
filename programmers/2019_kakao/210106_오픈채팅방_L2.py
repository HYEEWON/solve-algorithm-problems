from collections import defaultdict
def solution(record):
    answer = []
    d = defaultdict(str)
    index = defaultdict(list)
    for i in range(len(record)):
        record[i] = record[i].split()

    for r in record:
        if r[0] == 'Enter':    
            if d[r[1]] != '' and r[2] != d[r[1]]:
                for i in index[r[1]]:
                    answer[i] = r[2]+answer[i][answer[i].find('님'):]
            answer.append(r[2]+"님이 들어왔습니다.") 
            d[r[1]] = r[2]      
            index[r[1]].append(len(answer)-1)
        elif r[0] == "Leave":
            answer.append(d[r[1]]+"님이 나갔습니다.")
            index[r[1]].append(len(answer)-1)
        else: #Change
            d[r[1]] = r[2]
            for i in index[r[1]]:    
                answer[i] = d[r[1]]+answer[i][answer[i].find('님'):]
    return answer

# 대부분 통과, 시간 초과 있음
def solution2(record):
    answer, result = [], []
    d = defaultdict(str)
    for i in range(len(record)):
        record[i] = record[i].split()

    for r in record:
        if r[0] == 'Enter':
            if d[r[1]] == '':
                pass
            else:
                if r[2] != d[r[1]]:
                    for i in range(len(result)):
                        if r[1] == result[i][1]:
                            result[i][0] = r[2]+result[i][0][result[i][0].find('님'):]
            result.append([r[2]+"님이 들어왔습니다.", r[1]]) 
            d[r[1]] = r[2]      
        elif r[0] == "Leave":
            result.append([d[r[1]]+"님이 나갔습니다.", r[1]])
        else: #Change
            d[r[1]] = r[2]
            for i in range(len(result)):
                if r[1] == result[i][1]:
                    result[i][0] = d[r[1]]+result[i][0][result[i][0].find('님'):]
    for r in result:
        answer.append(r[0])
    return answer

#(*) 결과론적 풀이
def solution3(record):
    answer = []
    dic = defaultdict(str)
    for r in record:
        s = r.split()
        if len(s) > 2:
            dic[s[1]] = s[2]

    for r in record:
        s = r.split()
        if s[0] ==  'Enter':
            answer.append(dic[s[1]]+"님이 들어왔습니다.")
        elif s[0] == 'Leave':
            answer.append(dic[s[1]]+"님이 나갔습니다.")
    return answer
    
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))