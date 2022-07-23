class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        two variable to keep track of the range of VALID possibilites
        one var will always choose ) for wildcards, the other will choose (
        if the one choosing ( ever goes negative, return false from the whole func
        if ) goes negative, reset back to 0, because you could have just left that to be ""
        if 0 is in the range created from the two vars, return true
        """
        conservative, liberal = 0, 0
        for c in s:
            if c == ")":
                conservative -= 1
                liberal -= 1
            elif c == "(":
                conservative += 1
                liberal += 1
            else: # wildcard
                conservative -= 1
                liberal += 1
            
            if conservative < 0:
                conservative = 0
            if liberal < 0:
                return False
            
        return 0 in range(conservative, liberal + 1)
    
    
    def checkValidString_TOPDOWN(self, s: str) -> bool:
        memo = {}
        def backtrack(i, open_left):
            key = (i, open_left)
            if key in memo:
                return memo[key]
            if i == len(s) and open_left == 0:
                return True
            if i == len(s) and open_left != 0:
                return False
            if open_left < 0:
                return False
            
            if s[i] == "(":
                if backtrack(i + 1, open_left + 1):
                    memo[key] = True
                    return True
            elif s[i] == ")":
                if backtrack(i + 1, open_left - 1):
                    memo[key] = True
                    return True
            else: # wildcard
                if (backtrack(i + 1, open_left) or # treat as empty
                    backtrack(i + 1, open_left + 1) or # treat as an open
                    backtrack(i + 1, open_left - 1)): # treat as a close
                    memo[key] = True
                    return True
                
            memo[key] = False
            return False
        
        return backtrack(0, 0)