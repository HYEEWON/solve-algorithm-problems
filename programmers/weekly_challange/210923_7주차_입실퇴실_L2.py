from collections import deque

def solution(enter, leave):
    answer = [0 for i in range(len(enter))]

    room = deque([enter[0]])
    e_idx, l_idx = 1, 0
    while room:
        while leave[l_idx] not in room and room[-1] != leave[l_idx] and e_idx < len(enter):
            room.append(enter[e_idx])
            e_idx += 1

        for p in room:
            if p == leave[l_idx]:
                answer[p-1] += len(room)-1
            else:
                answer[p-1] += 1

        room.remove(leave[l_idx])
        l_idx += 1
        if e_idx < len(enter)-1 and len(room) == 0:
            room.append(enter[e_idx])
            e_idx += 1
    return answer

print(solution([1,3,2], [1,2,3]))
print(solution([1,4,2,3], [2,1,3,4]))