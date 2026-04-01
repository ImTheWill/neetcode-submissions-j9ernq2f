class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        intChecker = set()
        for x in nums:
            if x in intChecker:
                return True
            else: 
                intChecker.add(x)
        return False