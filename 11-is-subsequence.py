class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True
        
        if len(s) and len(t) == 1:
            if s[0] == t[0]:
                return True
            else:
                return False
            
        chars = []

        while i < len(s) and j < len(t):
            
            if s[i] == t[j]:
                chars.append(s[i])
                i += 1
                j += 1
            else:
                j += 1

        ans = ''.join(chars)

        if ans == s:
            return True
        else:
            return False