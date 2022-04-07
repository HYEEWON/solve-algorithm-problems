# Array, Two Pointers, Sorting

# 처음에 23~26의 while 문을 추가하지 않아서 시간 초과 발생
# 추가 후, 통과

class Solution:
    def threeSum(self, nums):
        answer = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            p1, p2 = i + 1, len(nums) - 1

            while 0 <= p1 < p2 < len(nums):
                three_sum = nums[i] + nums[p1] + nums[p2]
                if three_sum < 0:
                    p1 += 1
                elif three_sum > 0:
                    p2 -= 1
                else:
                    tmp = sorted([nums[i], nums[p1], nums[p2]])
                    if tmp not in answer:
                        answer.append(tmp)
                    while p1<p2 and nums[p1]==nums[p1+1]:
                        p1 += 1
                    while p1<p2 and nums[p2]==nums[p2-1]:
                        p2 -= 1
                    p1 += 1
                    p2 -= 1
        return answer

