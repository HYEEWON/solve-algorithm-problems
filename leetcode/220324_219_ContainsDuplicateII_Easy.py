# Array, Sliding Window, Hash Table

class Solution:
    # Sliding Window 풀이
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            if len(window) >= k:
                window.remove(nums[i - k])

            window.add(nums[i])
        return False
    
    # 마지막 인덱스를 저장
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        last_indexes = {}
        for i in range(len(nums)):
            if nums[i] in last_indexes.keys():
                if last_indexes[nums[i]] + k >= i:
                    return True
            last_indexes[nums[i]] = i
        return False
