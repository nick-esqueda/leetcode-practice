class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        treat the array like one big circle - 1st index is neighboring the 2nd index
        """
        if len(nums) <= 2:
            return max(nums)
        
        return max(self.rob_w_subarray(nums[1:]), self.rob_w_subarray(nums[:len(nums) - 1]))
    
    def rob_w_subarray(self, nums):
        one, two = 0, 0
        for num in nums:
            temp = max(two, num + one)
            one = two
            two = temp
        return two
        