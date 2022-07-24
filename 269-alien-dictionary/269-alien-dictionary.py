class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        return the alphabet of the alien language in order, unless you can't determine the order, so return ""
        if the graph has a cycle, then you can't determine the order of those letters
        
        
        BUILDING THE GRAPH:
        can only determine if a letter comes before the other if all previous letters are the same
        if you run out of chars in string2 and string2 is a prefix of string1, that is out of order, return ""
        if you run out of chars in string1 (i > len(string1)) just continue on to the next pair of strings
        
           i
        wrt
        wrf
        er
        ett
        rftt
        w -> e -> r -> t -> f

        z
        x
        z
        z <-> x
        """
        adj = dict()
        
        # put every letter into the adj list
        for word in words:
            for char in word:
                adj[char] = []
                
        # fill out the neighbors in the adj list
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            if len(w2) < len(w1) and w1[:len(w2)] == w2:
                return ""
            
            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]
                if w1[:j] != w2[:j] or c1 == c2: # continue if the prefixes of both words aren't the same (can't determine order), or chars are the same
                    continue
                adj[c1].append(c2)
                
                
        def get_topsort(char):
            if char in path:
                return False
            if char in done:
                return True
            
            path.add(char)
            for nei in adj[char]:
                if get_topsort(nei) is False:
                    return False
            stack.append(char)
            path.remove(char)
            done.add(char)
                
        stack = []
        done = set()
        for char in adj:
            path = set()
            if get_topsort(char) is False:
                return ""
            
        topsort = []
        while stack:
            topsort.append(stack.pop())
        return ''.join(topsort)
