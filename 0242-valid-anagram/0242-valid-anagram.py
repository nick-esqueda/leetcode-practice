class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return self.map_counts(s, t)
        return self.arr_count(s, t)

    def arr_count(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        diff = [0] * 26
        for i in range(len(s)):
            diff[ord(s[i]) - ord('a')] += 1
            diff[ord(t[i]) - ord('a')] -= 1
            
        return not any(diff)
        
    
    def map_counts(self, s: str, t: str) -> bool:
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