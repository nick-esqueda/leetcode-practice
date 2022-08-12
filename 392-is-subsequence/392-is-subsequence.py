class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        if s is bigger than t, return false immediately
        
        if you exit string t and the s pointer isn't at the end, return false
        if at any point the s pointer has reached the end, return true
        """
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        
        i = 0
        for t_char in t:
            if t_char == s[i]:
                i += 1
            if i == len(s):
                return True
        return False