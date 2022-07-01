class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        to see if something is a palindrome, you can start from the 'middle' (i) and spread outwards, checking if both chars are same
        you will do this for every char
        *this will only work for odd lengths of s
        for even lengths of s:
        take groups of two and spread outwards in the same manner
        always be keeping track of a maximum
        """
        pali_idx = (0, 0)
        
        # odds
        for i in range(len(s)):
            pi, pj = self.get_pali(s, i)
            pali_idx = (pi, pj) if pj - pi > pali_idx[1] - pali_idx[0] else pali_idx
        
        # evens
        for i in range(len(s)):
            j = i + 1
            pi, pj = self.get_pali(s, (i, j))
            pali_idx = (pi, pj) if pj - pi > pali_idx[1] - pali_idx[0] else pali_idx
        
        i, j = pali_idx
        return s[i:j + 1]
        
        
    def get_pali(self, s, mid):
        i, j = mid if isinstance(mid, tuple) else (mid, mid)
        
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                i, j = i - 1, j + 1
            else:
                break
        i, j = i + 1, j - 1
        return i, j