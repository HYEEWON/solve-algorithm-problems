dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

pose = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
left_pos = (3, 0)
right_pos = (3, 2)

def get_dist(cur, pos):
    return abs(cur[0]-pos[0]) + abs(cur[1]-pos[1])

def solution(numbers, hand):
    global left_pos, right_pos
    answer = ''
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left_pos = pose[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            right_pos = pose[n]
        else:
            left_dist = get_dist(left_pos, pose[n])
            right_dist = get_dist(right_pos, pose[n])

            if (left_dist < right_dist) or (left_dist == right_dist and hand == "left"):
                answer += 'L'
                left_pos = pose[n]
            elif left_dist > right_dist or (left_dist == right_dist and hand == "right"):
                answer += 'R'
                right_pos = pose[n]

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))