class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L,R,res, prev = 0,1,1, ""

        # we use prev to denote the previous equality value , we start right at index 1 so we can check that value
        # we have a result variable that we check every iteration where we increment only when we find a subarray larger than 
        #result  and replace it

        while R < len(arr):
            if arr[R-1] > arr[R] and prev != ">":
                res = max(res, R-L+1)
                R+=1
                prev = ">"
            elif arr[R-1] < arr[R] and prev != "<":
                res = max(res, R-L+1)
                R+=1
                prev = "<"
            else: 
                R = R+1 if arr[R] == arr[R-1] else R # handling same values = so skipping it if it is else keep r the same
                L = R-1
                prev = ""
        return res
