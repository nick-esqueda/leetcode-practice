class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [21, 21, 1, 1, 22]
         i
         
        each tab index will be the max of either -
            > the position right after the curr index
            > the sum of the num at this index + the num at i + 2
        """
        if len(nums) <= 2:
            return max(nums)
        
        nums[-2] = max(nums[-2], nums[-1])        
        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i + 1],
                          nums[i] + nums[i + 2])
            
        return nums[0]
        