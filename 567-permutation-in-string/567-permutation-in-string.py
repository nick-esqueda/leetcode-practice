class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        create a map of s1
        declare a map for s2
        loop a window of size len(s1) through s2
            on each iteration, remove the char at i and add char at j
            check if the two maps are equal
        """
        def remove_item(char):
            if s2_map[char] > 0:
                s2_map[char] -= 1
            else:
                del s2_map[char]
        
        def add_item(char):
            if char in s2_map:
                s2_map[char] += 1
            else:
                s2_map[char] = 1
        
        s1_map = collections.Counter(s1)
        i, j = 0, len(s1) - 1
        s2_map = collections.Counter(s2[i:j])
        while j < len(s2):
            add_item(s2[j])
            if s2_map == s1_map:
                return True
            i += 1
            j += 1
            remove_item(s2[i - 1])
                
        return False
                