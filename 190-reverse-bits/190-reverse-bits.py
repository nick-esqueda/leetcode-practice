class Solution:
    def reverseBits(self, n: int) -> int:
        """
        save a starting 0
        save the last bit and right shift 
        & the starting 0 with saved bit, and then left shift
        """
        rtn = 0
        for place in range(31, -1, -1):
            bit = (n & 1) << place
            rtn = rtn | bit
            n = n >> 1
        return rtn