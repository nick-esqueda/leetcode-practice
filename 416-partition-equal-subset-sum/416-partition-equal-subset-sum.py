class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        """
        if sum(nums) / 2 != sum(nums) // 2:
            return False
        target = sum(nums) // 2
        
        def find_sum(i, target, memo):
            key = (i, target)
            if key in memo:
                return memo[key]
            if target < 0 or i >= len(nums):
                return False
            if target == 0:
                return True
            
            num = nums[i]
            if (find_sum(i + 1, target - num, memo) or
                find_sum(i + 1, target, memo)):
                memo[key] = True
                return True
            
            memo[key] = False
            return False
                        
        return find_sum(0, target, {})