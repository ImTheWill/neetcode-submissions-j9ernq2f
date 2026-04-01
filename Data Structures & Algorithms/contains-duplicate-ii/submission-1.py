class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = {}

        for i in range(len(nums)):
            if nums[i] in window and abs(window[nums[i]] - i) <= k :
                return True;
            else:
                window[nums[i]] = i
        return False

