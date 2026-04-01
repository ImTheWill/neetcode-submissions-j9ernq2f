class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum,curMax = nums[0], 0;
        minSum, curMin = nums[0], 0
        total = 0;

        for i in range(len(nums)):
            total += nums[i]
            curMin = min(curMin + nums[i], nums[i])
            curMax = max(curMax + nums[i], nums[i])
            minSum = min(minSum, curMin);
            maxSum = max(maxSum, curMax);
        
        return max(maxSum, total-minSum) if maxSum > 0 else maxSum