class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        want the count of odd numbers - INCLUDING the two boundaries
        
        o  o
        3, 7
        range = 4
        > 3 odds
        
        e  e
        4, 8
        range = 4
        > !!! only 2 odds between here!
        
        e  o
        4, 9
        range = 5
        > 3 odds
        
        o  e
        3, 8
        range = 5
        > 3 odds
        
        take the floor of the range, add 1?
        unless both nums are even
        
        low  |  high
          o  |  o
          e  |  e
          e  |  o
          o  |  e
        """
        
        if (high % 2 == 0) and (low % 2 == 0):
            return (high - low) // 2
        return ((high - low) // 2) + 1