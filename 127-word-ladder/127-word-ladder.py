class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        for each word in words, generate patterns by replacing a char with a wildcard - O(nm)
        map each pattern to that word (use a set as value)
        then, you'll have a adjlist/map with patterns as keys and all words that match that pattern as values
        to find the neighbors of a word:
            you first have to find all of it's patterns
            with those patterns, key into the adjlist at every pattern
            the sum of all of those words in each pattern (minus itself) are the neighbors
            can use a set to hold all of those neighbors and remove the word you used to key into it from that set
        can maybe reconstruct the original map this way - O(nm^2)
        time complexity :
            you're looping through each word - n
            for each word, youre getting all of the patterns that you made of that word - 1 if you have a set of those already
            create a set to store all neis
            with those patterns you key into the adjlist and put each word into the set - n?
            you do that for all patterns - m
            after getting all of those neis, remove the word you looked for from the set, and then add that as a KV pair to a real adjlsit 
            
        *ot: [hot, dot, lot]
        h*t: [hot, hit]
        ho*: [hot]
        hot: set(dot, lot, hit)
        """
        wordList.append(beginWord)
        pattern_adj = defaultdict(set)
        word_to_patterns = {}
        for word in wordList:
            patterns = set()
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                patterns.add(pattern)
                pattern_adj[pattern].add(word)
            word_to_patterns[word] = patterns
            
        adj = {}
        for word in wordList:
            neis = set()
            for pattern in word_to_patterns[word]:
                pattern_neis = pattern_adj[pattern]
                for nei in pattern_neis:
                    neis.add(nei)
            neis.remove(word)
            adj[word] = neis
            
        q = deque([(beginWord, 1)])
        vis = set(beginWord)
        while q:
            word, dist = q.popleft()
            print(word)
            if word == endWord:
                return dist
            for nei in adj[word]:
                if nei not in vis:
                    vis.add(nei)
                    q.append((nei, dist + 1))
        return 0
