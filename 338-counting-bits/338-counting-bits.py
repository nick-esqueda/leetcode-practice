class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        from 0 up to n inclusive (i), calculate how many 1's are in the binary representation of i and store that in the array at that same index
        
        can have a helper method to find how many 1's are in each int, and call it on every iteration up to n
        """
        rtn = []
        for i in range(n + 1):
            rtn.append(self.num_ones(i))
        return rtn
    
    def num_ones(self, n):
        count = 0
        while n != 0:
            if n & 1:
                count += 1
            n = n >> 1
        return count