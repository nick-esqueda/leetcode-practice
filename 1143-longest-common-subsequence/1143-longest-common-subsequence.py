class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        start at the base cases.
        dp(i, j) = 0                                <--- if i == len(text1) || j == len(text2)        
        dp(i, j) = 1 + dp(i + 1, j + 1)             <--- if text1[i] == text2[j]
        dp(i, j) = max(dp(i + 1, j), dp(i, j + 1))  <--- if text1[i] != text2[j]
        """
        l1, l2 = len(text1), len(text2)
        tab = [[0] * (l2 + 1) for _ in range(l1 + 1)] # +1 to allow for loops to hit base cases.
        
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    tab[i][j] = 1 + tab[i + 1][j + 1]
                else:
                    tab[i][j] = max(tab[i + 1][j], tab[i][j + 1])
        return tab[0][0]
        
        
    def longestCommonSubsequence_TOPDOWN(self, text1: str, text2: str) -> int:
        """
        PROBLEM:
        want to go through each string and look for the longest subsequence that are the same in both strings
        
        STATE VARIABLES:
        i - position in text1
        j - position in text2
        
        SUBPROBLEMS:
        return the longest common subsequence starting at i and j
        
        BASE CASES:
        if one of the strings is empty, return 0
        
        RECURRENCE RELATION:
        if there is a match, then LCS here is 1 + max(the LCS of incrementing i, the LCS from incrementing j)
        if there is no match, then 0 + ...
        dp(i, j) = 0                                <--- if i == len(text1) || j == len(text2)        
        dp(i, j) = 1 + dp(i + 1, j + 1)             <--- if text1[i] == text2[j]
        dp(i, j) = max(dp(i + 1, j), dp(i, j + 1))  <--- if text1[i] != text2[j]
        """
        memo = {}
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            key = (i, j)
            if key not in memo:
                if text1[i] == text2[j]:
                    memo[key] = 1 + dp(i + 1, j + 1)
                else:
                    memo[key] = max(dp(i + 1, j), dp(i, j + 1))
            return memo[key]
        
        return dp(0, 0)