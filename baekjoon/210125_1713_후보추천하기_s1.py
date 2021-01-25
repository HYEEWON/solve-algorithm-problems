N = int(input())
number = int(input())
students = list(map(int, input().split()))

candidates = []
counts = []
for student in students:
    if len(candidates) < N:
        if student not in candidates:
            candidates.append(student)
            counts.append(1)
        else:
            counts[candidates.index(student)] += 1
    else:
        if student in candidates:
            counts[candidates.index(student)] += 1
        else:
            minIndex = counts.index(min(counts))
            counts.pop(minIndex)
            candidates.pop(minIndex)

            counts.append(1)
            candidates.append(student)

candidates.sort()
for c in candidates:
    print(c, end=' ')