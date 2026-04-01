class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        subHashIndex = []
        for i in range(len(strs)):
            subHash = {}
            for j in range(len(strs[i])):
                subHash[strs[i][j]] = 1 + subHash.get(strs[i][j], 0)
            if subHash in subHashIndex:
                index = subHashIndex.index(subHash)
                result[index].append(strs[i])
            else:
                subHashIndex.append(subHash)
                result.append([strs[i]])
        return result