# Array, Two Pointer, Greedy

# 틀린 이유
# 포인터를 이동하는 기준을 생각하지 못함 (while 안의 if문 부분)
# 투 포인터로 O(N)에 풀이 가능

class Solution:
    def maxArea(self, height):
        answer = 0
        start, end = 0, len(height)-1

        while start < end:
            answer = max(answer, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return answer

    # 시간 초과
    def maxArea2(self, height):
        answer = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                answer = max(answer, min(height[i], height[j])*(j-i))
        return answer

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))