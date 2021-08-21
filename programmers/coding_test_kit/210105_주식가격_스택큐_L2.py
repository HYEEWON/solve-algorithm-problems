# 스택을 사용하는 방법
def solution(prices):
    answer = [0 for i in range(len(prices))]
    st = [0]
    for i in range(len(prices)):
        while len(st) > 0 and prices[i] < prices[st[-1]]:
            top = st.pop()
            answer[top] = i-top
        st.append(i)
        
    while len(st) > 0:
        top = st.pop()
        answer[top] = len(prices)-top-1
    return answer

# 스택을 사용하지 않고 하나씩 비교하는 방법
def solution2(prices):
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break
    return answer

print(solution([1, 2, 3, 2, 3]))