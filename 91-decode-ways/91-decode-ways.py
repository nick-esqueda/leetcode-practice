class Solution:
    def numDecodings(self, s: str):
        """
        
        """
        tab = { len(s): 1 }
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                tab[i] = 0
            else:
                tab[i] = tab[i + 1]
                
            if (i + 1 < len(s) and 
               ( s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                tab[i] += tab[i + 2]
        return tab[0]
        
        
    
    def numDecodings_TOPDOWN(self, s: str) -> int:
        """
        11206
        2190
        
        if current num is a 0, cannot use it
            ? will this situation ever happen if you take care of it in the if conditionals?
        if the second num is a 0, you MUST take the second num with the first
        
        if current num is a 1, can choose to take it alone, or also include the 2nd num
        if current num is a 2, can choose to take it alone, or also include 2nd num ONLY IF that 2nd num <= "6"
        if current num is the last in s, can only take it alone
        
        can't take both nums if the first num is two and the second is > 6
        """
        valid_second = "0123456"
        def backtrack(i, memo):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            
            count = 0
            count += backtrack(i + 1, memo)
            if (i + 1 < len(s) and 
                ((s[i] == "1") or (s[i] == "2" and s[i + 1] in valid_second))):
                count += backtrack(i + 2, memo)
            
            memo[i] = count
            return memo[i]
        
        return backtrack(0, {})

