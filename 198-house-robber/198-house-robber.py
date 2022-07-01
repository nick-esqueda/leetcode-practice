class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        can choose to either rob this one and skip the next
        or can choose to skip this one and rob the next one
        
        the max you can rob of the first house is just that value, and the same for the second 
        """
        if len(nums) <= 2:
            return max(nums)
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])

        return nums[-1]