class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pali_len(l, r):
            pali_len = 0
            while (l >= 0 and r < len(s)) and (s[l] == s[r]):
                pali_len = r - l + 1
                l, r = l - 1, r + 1
            return (l + 1, r - 1)
        
        
        longest = 0, 0
        # EVENS
        for i in range(len(s)):
            l, r = pali_len(i, i)
            if (r - l + 1) > (longest[1] - longest[0] + 1):
                longest = l, r
        
        # ODDS
        for i in range(len(s) - 1):
            l, r = pali_len(i, i + 1)
            if (r - l + 1) > (longest[1] - longest[0] + 1):
                longest = l, r
        
        l, r = longest
        return s[l:r + 1]
            
        
    
    def longestPalindrome_BRUTE_FORCE(self, s: str) -> str:
        def is_pali(ss):
            return ss == ss[::-1]
        
        longest = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_pali(s[i:j + 1]) and j - i > len(longest):
                    longest = s[i:j + 1]
                    
        return longest
        
