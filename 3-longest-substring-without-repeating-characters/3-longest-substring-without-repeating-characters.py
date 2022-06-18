class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        move i up to j if j == j - 1
        max = max(max, j - i + 1)
        """
        
        max_len = 0
        i, j = 0, 0
        chars = set()
        while j < len(s):
            if s[j] not in chars:
                max_len = max(max_len, j - i + 1)
                chars.add(s[j])
                j += 1
            else:
                chars.remove(s[i])
                i += 1
                # j += 1
                
        return max_len
            