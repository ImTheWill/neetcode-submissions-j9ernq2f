class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #return an array of size two that contains the indices 
        #that are not equal and add up to target
        R=0
        L=len(numbers)-1
        while R<L:
            currSum = numbers[R] + numbers[L] 
            if currSum ==target:
                return [R+1, L+1]
            if currSum > target:
                L-=1
            else:
                R+=1


                



        