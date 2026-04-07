class Solution:
    def isPalindrome(self, s: str) -> bool:
        #string formatting
        s =  s.lower()
        s = s.replace(" ", "")
        s = s.replace("'", "")
        s = s.replace(",", "")
        s = s.replace("!", "")
        s = s.replace("?", "")
        s = s.replace(".", "")
        s = s.replace(":", "")
        s = s.replace(";", "")
        
        
        if len(s) ==0:
            return True
        
        R = len(s)-1
        for i in range(len(s)):
            if i > R:
                return True
            else:
                if s[i] != s[R]:
                    return False
                else:
                    R-=1
        return True

