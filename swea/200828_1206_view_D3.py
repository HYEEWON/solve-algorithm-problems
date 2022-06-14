for t in range(10):
    n = int(input())
    building = list(map(int, input().split()))
    cnt = 0
    for idx in range(2, n-2):
        front = max(building[idx-2: idx])
        back = max(building[idx+1: idx+3])
        if building[idx] > front and building[idx] > back:
            cnt += building[idx] - max(front, back)
    print('#'+str(t+1)+' '+str(cnt))