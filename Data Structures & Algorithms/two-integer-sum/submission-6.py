class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}
        for i in range(len(nums)):
            findNum = target- nums[i]
            if findNum in numMap:
                return [numMap.get(findNum), i]
            else: numMap[nums[i]] = i
        return []