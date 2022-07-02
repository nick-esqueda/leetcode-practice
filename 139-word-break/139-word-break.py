class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        whenever i is right after the end of the string, output is True
        decrement backwards through s
        check s starting at i if that substr .startswith the word
        if it does, check the tab at i + len(str), and if it's True, set the tab at this i to True, else False
        keep iterating backwards
        after iterating return the value you have for tab[0]
        """
        tab = [False] * (len(s) + 1)
        tab[-1] = True
        
        for i in range(len(s)-1, -1, -1):
            substr = s[i:]
            for word in wordDict:
                if substr.startswith(word) and tab[i + len(word)] is True:
                    tab[i] = True
                    break
        return tab[0]
        
        
    
    
    def wordBreak_TOPDOWN(self, s: str, wordDict: List[str]) -> bool:
        """
        can choose only words that .startswith the front of the word
        can use an i pointer to indicate where to start the rest of s
        once you find a match, move i up by the length of the word from wordDict
        if i is the length of s, return True
        if i is greater than the length of s, you took a word that was too big, so return False
        if you go through all words in wordDict and didn't find a .startswith, return False
        """
        def can_complete(i, memo):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            if i > len(s):
                return False
            
            substr = s[i:]
            for word in wordDict:
                if substr.startswith(word):
                    if can_complete(i + len(word), memo):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False
        
        return can_complete(0, {})