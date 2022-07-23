class Solution:
    def checkValidString(self, s: str) -> bool:
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