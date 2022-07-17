class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        to find if there is a 1 in a certain position, you can & the integer with whatever byte has only a 1 in the place you are looking for
        you COULD & n with a new number representing each position each time, but then you'd have to calculate the power of 2 for each position
        a more efficient way to do it would be to right shift once for every position to see if it &'s with 1 every time
        """
        count = 0
        for i in range(32):
            if n & 1:
                count += 1
            n = n >> 1
        return count