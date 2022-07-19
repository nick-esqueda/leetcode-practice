class Solution:
    def reverse(self, x: int) -> int:
        """
        can mod by 10 to get the ones place.
        can divide by 10 (//) to get rid of the ones place/shift over to the right
        can multiply the res num by 10 to shift to the right and add the ones place of the old num
        need to check if the new num is about to be outside of the range
        
        need to use fmod because python doesn't take the modulo of negative numbers like C langs do
        """
        MAX = 2**31 - 1
        MIN = -2**31
        rtn = 0
        while x != 0:
            digit = int(math.fmod(x, 10)) # need to make int because fmod returns float
            x = int(x / 10) # can't do // because it behaves weird with negatives in python
            
            if ((rtn == (MAX // 10) and digit > 7) or 
                rtn > (MAX // 10)):
                return 0
            if ((rtn == int(MIN / 10) and digit < -8) or 
                rtn < int(MIN / 10)):
                print(rtn, MIN)
                return 0
            
            rtn = (rtn * 10) + digit
            
        return rtn
        