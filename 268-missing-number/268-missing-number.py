class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        if you xor together all numbers in one group, and xor everything in a duplicate group, then xor those two results together,
            you will end up with 0, since "all of the duplicates cancel out"
        but, if you leave a number out of one of those groups, then that number will be leftover when you xor the two results
        """
        rtn = 0
        for num in nums:
            rtn = rtn ^ num
        
        compare = 0
        for i in range(len(nums) + 1):
            compare = compare ^ i
            
        return rtn ^ compare