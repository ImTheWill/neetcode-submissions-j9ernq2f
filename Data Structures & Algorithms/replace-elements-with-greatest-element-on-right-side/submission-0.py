class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = -1;
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > currMax:
                temp = arr[i]
                arr[i] = currMax
                currMax = temp
            else:
                arr[i] = currMax
        return arr
            