class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        your tab will be a 2D grid len(s1) x len(s2)
        starting from the bottom right, calculate the LCS for each position
        there's a row and a column for each letter, plus a 'base case' row and column filled with 0's
        each position represents the LCS for the substrings starting at the row and col indices respectively
        if the start of both substrs are equal (a new match), add 1 to the LCS in the bottom right diagonal
            - b/c if you find a match, you increment both i and j and add that match to the total
        otherwise, just take the max of either the right or down position (incrementing i or j)
        """
        tab = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range(len(text1)-1, -1, -1): # i = rows
            for j in range(len(text2)-1, -1, -1): # j = cols
                if text1[i] == text2[j]:
                    tab[i][j] = 1 + tab[i + 1][j + 1]
                else:
                    tab[i][j] = max(tab[i + 1][j], tab[i][j + 1])
        return tab[0][0]
            
    
    
    def longestCommonSubsequence_TOPDOWN(self, text1: str, text2: str) -> int:
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