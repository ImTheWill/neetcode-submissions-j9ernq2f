class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        if len(s) != len(t):
            return False;
        if len(s) == 0:
            return True;

        for i in range(len(s)):
            if s[i] in dictS:
                dictS[s[i]] = dictS[s[i]] + 1
            else:
                dictS[s[i]] = 1

            if t[i] in dictT:
                dictT[t[i]] = dictT[t[i]] + 1
            else:
                dictT[t[i]] = 1

        for key, value in dictS.items():
            if key not in dictT:
                return False;
            if dictT[key] != value:
                return False;
        return True;
