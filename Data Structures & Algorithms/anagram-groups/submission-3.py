class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainMap = {}
        for i in range(len(strs)):
            
            sortedString = ''.join(sorted(strs[i])) #|| tuple(sorted(strs[i]))
            if sortedString in mainMap: 
                mainMap[sortedString].append(strs[i])
            else:
                mainMap[sortedString] = [strs[i]]
        return list(mainMap.values()) #make a list of whatever values