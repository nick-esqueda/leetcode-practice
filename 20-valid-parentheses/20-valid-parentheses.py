class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        """
        """
        create a hashtable to associate closing and opening parens with each other
        create a stack to check that corresponding parens close each other
        iterate through string
        if i is an open paren, push it to the stack and keep iterating
        if i is in the hashtable (meaning it's a closing) closeing paren...
          if there's nothing on the stack, the closing doesn't match anything, return false
          if what's at the top of the stack is not the associated paren in the map, return false
        once you go through the whole string, check if the stack has something on it.
        if so return false else true
        """
        
        map = {
          ")": "(",
          "]": "[",
          "}": "{"
        }
        
        sta = [];
        
        for char in s:
          if char not in map:
            sta.append(char)
          else:
            if sta and map[char] == sta[-1]:
              sta.pop()
            else:
              return False
          
        return len(sta) == 0
        
        
        