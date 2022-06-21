class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        declare a defaultdict(int)
        while j < len(s)
            increment s[j] in defaultdict
            reassign max_count by looping through manually every time (is this necessary?)
                                        if s[j] > max count, reassign?
            flips_needed = len(j - i + 1) - max_count
            if flips_needed <= k:
                reassign longest accordingly with len(j - 1 + 1)
                increment j
            else:
                s[i] -= 1
                s[j] -= 1 (in order to compensate for the increment at beginning of loop)
                increment i
        
        OPTIMIZATION:
        should you instead, have a map with counts as keys and letters of that count as values?
        max count could ever be would be is len(s), and since we're already iterating through whole string, can do this anyways
        """
        counts = collections.defaultdict(int)
        max_count = 0
        longest = 0
        i, j = 0, 0
        while j < len(s):
            counts[s[j]] += 1
            for letter in counts:
                max_count = max(counts[letter], max_count)
                
            substr_len = j - i + 1
            flips_needed = substr_len - max_count
            if flips_needed <= k:
                longest = max(substr_len, longest)
                j += 1
            else:
                counts[s[i]] -= 1
                counts[s[j]] -= 1
                i += 1
        return longest