import sys

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    people, answer = [], []

    for n in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())
        people.append([a, b])

    people.sort()
    answer.append(people[0])
    
    for i in range(1, N):
        if not (answer[-1][0] < people[i][0] and answer[-1][1] < people[i][1]):
            answer.append(people[i])

    sys.stdout.write(str(len(answer)) + '\n')