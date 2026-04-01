class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tMap, sMap = {}, {}
        if len(s) != len(t):
            return False

        for i in range (len(s)): 
            if s[i] in sMap:
                sMap[s[i]] += + 1
            else:
                sMap[s[i]] = 1;
        for i in range (len(t)):
            if t[i] in tMap:
                tMap[t[i]] += + 1
            else:
                tMap[t[i]] = 1;
        
        for item in sMap:
            if item not in tMap:
                return False
            if sMap[item] != tMap[item]:
                return False
        return True