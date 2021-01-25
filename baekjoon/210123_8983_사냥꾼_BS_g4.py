# pypy3로 통과, python3는 시간초과
M, N, L = map(int, input().split())
pos = map(int, input().split())
pos = sorted(pos)

animal = []
for i in range(N):
    ins = list(map(int, input().split()))
    if ins[1] > L or ins[0]<pos[0]-L or ins[0]>pos[-1]+L:
        continue
    animal.append(ins) # x, y
animal = sorted(animal)

cnt = 0
for a in animal:
    start = 0
    end = len(pos)-1
    while start <= end:
        mid = (start+end)//2
        distance = abs(pos[mid]-a[0])+a[1]
        if distance > L:
            if pos[mid] <= a[0]: # 왼쪽제거
                start = mid+1
            else:
                end = mid-1
        else:
            cnt += 1
            break
print(cnt)

#(*) python3도 통과
M, N, L = map(int, input().split())
pos = map(int, input().split())
pos = sorted(pos)

animal = []
for i in range(N):
    ins = list(map(int, input().split()))
    if ins[1] > L or ins[0]<pos[0]-L or ins[0]>pos[-1]+L:
        continue
    animal.append(ins) # x, y
animal = sorted(animal)

cnt = 0
mid = 0
for a in animal:
    start = mid
    end = len(pos)-1
    while start <= end:
        mid = (start+end)//2
        if pos[mid] <= a[0]:
            if mid == len(pos)-1 or a[0] < pos[mid+1]:
                break
            start = mid+1
        else:
            end = mid-1
    if abs(pos[mid]-a[0])+a[1] <= L:
        cnt += 1
    elif mid+1<len(pos) and abs(pos[mid+1]-a[0])+a[1] <= L:
        cnt += 1
print(cnt)