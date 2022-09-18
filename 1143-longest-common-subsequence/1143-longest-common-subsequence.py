class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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
        dp(i, j) = 0                                     <--- if i == len(text1) || j == len(text2)        
        dp(i, j) = 1 + dp(i + 1, j + 1)   <--- if text1[i] == text2[j]
        dp(i, j) = max(dp(i + 1, j), dp(i, j + 1))       <--- if text1[i] != text2[j]
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