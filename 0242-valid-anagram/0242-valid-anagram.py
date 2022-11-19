class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = dict()
        t_map = dict()

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char not in s_map:
                s_map[s_char] = 0
            if t_char not in t_map:
                t_map[t_char] = 0
            
            s_map[s_char] += 1
            t_map[t_char] += 1

        return s_map == t_map