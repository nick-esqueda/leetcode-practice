class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        if you add up the indices of s1 and s2, you'll get the index in s3 that holds the remainder of the chars
        if you have a 2D tab with s1 and s2 chars as rows/cols, each pos will be a boolean whether or not you
            can interleave the remaining s1 and s2 chars together to make up the remainder of s3
        the bottom right diagonal will be True, since that's the case where you used all chars of both strings
        the bottommost and rightmost row and column represent the ability to create the rest of s3 with just one string
            - need to determine these manually / these are not base cases
        starting at the bottommost row, work backwards and calculate the index of s3 you need to look at
        at each position, calculate the s3 idx by adding both r and c together
        that s3 idx will be your char to match
        if none of the s1 or s2 chars match, set that pos to False
        if one of the chars match, look at the corresponding down or right pos, and set pos equal to whatever is in that pos
        if both of the chars match, look at both right and down pos's and if either is True, set pos to True
        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        s1 += '!'
        s2 += '!'
        tab = [[False] * (len(s1)) for _ in range(len(s2))]
        
        for r in range(len(s2) - 1, -1, -1):
            for c in range(len(s1) - 1, -1, -1):
                if r + c >= len(s3):
                    tab[r][c] = True
                    continue
                target = s3[r + c]
                if s2[r] == target and s1[c] == target:
                    tab[r][c] = tab[r + 1][c] or tab[r][c + 1] # either bottom or right
                elif s2[r] == target:
                    tab[r][c] = tab[r + 1][c] # look below
                elif s1[c] == target:
                    tab[r][c] = tab[r][c + 1] # look right
                else:
                    tab[r][c] = False # no matches - F
                    
        return tab[0][0]
                
            
        
        
        
    def isInterleave_TOPDOWN(self, s1: str, s2: str, s3: str) -> bool:
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