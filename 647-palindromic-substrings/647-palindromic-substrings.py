class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        can calculate the number by getting all odd and even palindromes
        iterate through s
        for each char, spread outwards to see if there are more palindromes
        increment count if you find one, and break if that spread didn't find a palindrome
        do the same for odds
        """
        count = 0
        for i in range(len(s)):
            
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l, r = l - 1, r + 1 
                else:
                    break
            
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l, r = l - 1, r + 1 
                else:
                    break
            
        return count
            