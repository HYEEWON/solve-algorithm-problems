import sys

N, M = map(int, sys.stdin.readline().strip().split())

room_name = []
room_reserved = []
room_empty = {}
room_flag = {}

for i in range(N):
    room_name.append(sys.stdin.readline().strip())

room_name.sort()

for i in range(M):
    room_reserved.append(list(map(str, sys.stdin.readline().strip().split())))
    room_reserved[i] = [room_reserved[i][0], int(room_reserved[i][1]), int(room_reserved[i][2])]

room_reserved = sorted(room_reserved, key=lambda x: (x[0], x[1]))

for i in range(N):
    room_empty[room_name[i]] = []
    room_flag[room_name[i]] = False

end = 9
for i in range(M):
    if not room_flag[room_reserved[i][0]]:
        if i > 0 and end != 18:
            room_empty[room_reserved[i - 1][0]].append([end, 18])
        room_flag[room_reserved[i][0]] = True
        end = 9

    if room_reserved[i][1] != end:
        room_empty[room_reserved[i][0]].append([end, room_reserved[i][1]])
    end = room_reserved[i][2]

if end != 18:
    room_empty[room_reserved[M - 1][0]].append([end, 18])

for i, name in enumerate(room_name):
    sys.stdout.write('Room ' + name + ':\n')
    if not room_flag[name]:
        sys.stdout.write('1 available:\n')
        sys.stdout.write('09-18\n')
        if i != N - 1:
            sys.stdout.write('-----\n')
        continue

    if not room_empty[name]:
        sys.stdout.write('Not available\n')
        if i != N - 1:
            sys.stdout.write('-----\n')
        continue

    sys.stdout.write(str(len(room_empty[name])) + ' available:\n')
    for t in room_empty[name]:
        if t[0] < 10:
            sys.stdout.write('0' + str(t[0]) + '-' + str(t[1]) + '\n')
        else:
            sys.stdout.write(str(t[0]) + '-' + str(t[1]) + '\n')
    if i != N - 1:
        sys.stdout.write('-----\n')