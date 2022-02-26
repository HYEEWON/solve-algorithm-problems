def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    a, b = 0, 0
    for size in sizes:
        if a < size[0]:
            a = size[0]
        if b < size[1]:
            b = size[1]
    return a*b

'''return max(max(x) for x in sizes) * max(min(x) for x in sizes)'''