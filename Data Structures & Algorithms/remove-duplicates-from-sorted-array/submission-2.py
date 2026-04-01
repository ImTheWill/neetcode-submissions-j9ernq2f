class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        values = set()

        i = 0;

        while i <len(nums):
            print(i)
            if nums[i] in values:
                nums.remove(nums[i])
                i -= 1
            else:
                values.add(nums[i])
                k+=1
            i +=1
        print(values)
        return k;