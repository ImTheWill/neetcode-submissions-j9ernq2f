class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = "" 
        for i in range(len(strs[0])):
            for s in strs:
                if len(s) == i or s[i] != strs[0][i]:
                #if char i at string s is not equal to the string[0][i] then we break and check bounds
                    return res;
            res += strs[0][i]
        return res;