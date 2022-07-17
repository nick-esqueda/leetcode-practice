class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        to find if there is a 1 in a certain position, you can & the integer with whatever byte has only a 1 in the place you are looking for
        you COULD & n with a new number representing each position each time, but then you'd have to calculate the power of 2 for each position
        """
        count = 0
        for i in range(32):
            mask = 2 ** i
            if (n & mask) != 0:
                count += 1
        return count                