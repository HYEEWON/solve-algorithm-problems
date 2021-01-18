def solution(triangle):
    answer = [[0]* (i+1) for i in range(len(triangle))]
    answer[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                answer[i][j] = answer[i-1][j] + triangle[i][j]
            elif j == i:
                answer[i][j] = answer[i-1][j-1] + triangle[i][j]
            else:
                answer[i][j] = max(answer[i-1][j-1] + triangle[i][j], answer[i-1][j] + triangle[i][j])
    return max(answer[-1])