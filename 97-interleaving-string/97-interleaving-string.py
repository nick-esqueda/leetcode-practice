class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        if start of both string are ==, must choose between either one to use
        if only one string starts with the first char in s3, have to use that one
        if neither string starts with the first char in s3, return False (s3 cannot be formed)
        if there are no more chars left in s3, return True
            ? what if there are still chars left in s1 and s2? should you return False instead?
                - if this is the case, check that s1 and s2 and s3 all have no more chars at same time
        if any recursive call comes back as True, return that True up the call stack
        """
        s1 += '!'
        s2 += '!'
        memo = {}
        def interleave(i, j, k):
            key = (i, j, k)
            if key in memo:
                return memo[key]
            if k >= len(s3):
                return i >= len(s1) - 1 and j >= len(s2) - 1
            
            char = s3[k]
            if s1[i] == char and s2[j] == char:
                memo[key] = (interleave(i + 1, j, k + 1) or
                            interleave(i, j + 1, k + 1))
                return memo[key]
            elif s1[i] == char:
                if interleave(i + 1, j, k + 1):
                    memo[key] = True
                    return True
            elif s2[j] == char:
                if interleave(i, j + 1, k + 1):
                    memo[key] = True
                    return True
                
            memo[key] = False
            return False
        
        return interleave(0, 0, 0)