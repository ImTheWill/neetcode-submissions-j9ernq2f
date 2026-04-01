class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            val = target- nums[i];
            if val in numMap and i != numMap[val]:
                return [numMap[val], i]
            else:
                numMap[nums[i]] = i