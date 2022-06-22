class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        while j < len(s):
            if need == have:
                replace shortest with (i, j) if i - j is less than curr shortest
                if i in t_map:
                    if i in window map is == i in t_map: 
                        decrement have
                    decrement i in window
                i += 1
            else:
                j += 1
                if j in t_map:
                    increment j in window map
                    if j in window map == j in t_map:
                        have += 1

                    
        if j gets to the end and you have yet to find all chars in t, return ""
        actually need to store the indices of the substr you found so that you can slice it out afterwards
        
        ???:
        move i until dont have what you need?
        as you're moving i up, constantly be reassigning shortest so that you catch everything
        """
        t_map = collections.Counter(t)
        window = { char: 0 for char in t_map } 
        
        shortest = (0, len(s) + 1)
        have, need = 0, len(t_map)
        i, j = 0, 0
        while j < len(s):
            char_j = s[j]
            
            if char_j in window:
                window[char_j] += 1
                if window[char_j] == t_map[char_j]:
                    have += 1
            
            while need == have:
                char_i = s[i]
                shortest = (i, j) if j - i < shortest[1] - shortest[0] else shortest
                
                if char_i in window and window[char_i] == t_map[char_i]: 
                    have -= 1
                if char_i in window:
                    window[char_i] -= 1
                i += 1
                
            j += 1
                        
        l, r = shortest
        return s[l:r + 1] if r < len(s) else ""
    
    
    
    
    