class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A man, a plan, a canal: Panama
             i                   j
        A man, a plan, a canal: Panama
        """
        i, j = 0, len(s) - 1
        while i < j:
            l_char, r_char = s[i].lower(), s[j].lower()
            if not l_char.isalnum():
                i += 1
                continue
            if not r_char.isalnum():
                j -= 1
                continue
            if l_char != r_char:
                return False
            i += 1
            j -= 1
        return True
            
            