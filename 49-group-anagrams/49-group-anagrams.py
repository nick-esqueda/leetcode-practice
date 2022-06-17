class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        """
        
        count_map = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        for s in strs:
            counts = [0] * 26
            for char in s:
                letter_idx = letters.index(char)
                counts[letter_idx] += 1
            
            counts_tup = tuple(counts)
            if counts_tup in count_map:
                count_map[counts_tup].append(s)
            else:
                count_map[counts_tup] = [s]
                
        return count_map.values()
