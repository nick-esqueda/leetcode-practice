class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        pointers for both strings
        if there is a match between i and j, move both pointers up
            add 1 to the recursive call
        if no match, can choose to either move i up, or j
        when a pointer goes out of bounds, return 0
        take the max of all recursive calls
        """
        def get_LCS(i, j, memo):
            key = (i, j)
            if key in memo:
                return memo[key]
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if text1[i] == text2[j]:
                memo[key] = 1 + get_LCS(i + 1, j + 1, memo)
                return memo[key]
            else:
                memo[key] = max(get_LCS(i + 1, j, memo), get_LCS(i, j + 1, memo))
                return memo[key]
        
        return get_LCS(0, 0, {})