class Solution:
    
    # 풀이
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                if nums[l] + nums[r] == target:
                    answer = [l, r]
                    break
            if answer:
                break
        return answer

    # 시간 단축 풀이, 참고한 풀이
    # 해시 테이블을 사용해 인덱스를 저장하여 사용
    def twoSum2(nums, target):
        answer = []
        indexes = {}
        for i in range(len(nums)):
            cur = nums[i]
            match = target - cur
            if match in indexes.keys():
                return [i, indexes[match]]
            else:
                indexes[cur] = i