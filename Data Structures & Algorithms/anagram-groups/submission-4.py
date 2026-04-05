class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = {}

        for i in range(len(strs)):
            currStr = tuple(sorted(strs[i]))
            if currStr in resMap:
                resMap[currStr].append(strs[i])
            else: resMap[currStr] = [strs[i]]

        return list(resMap.values())