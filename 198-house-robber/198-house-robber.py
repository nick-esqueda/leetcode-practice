class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        same as topdown, but starting at the beginning of the array by the base cases and iterating.
        RECURRENCE RELATION:
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        """
        if len(nums) == 1:
            return nums[0]
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
        return nums[-1]
        
    
    
    def rob_TOPDOWN(self, nums: List[int]) -> int:
        """
        is this a DP problem? yes, want to find the max of something based on decisions.
        subproblems:
            what is the max amount i can rob, up to and including this current house?
            MAIN PROBLEM: what is the max amount you can rob up to and including the last house/index?
        overlapping subproblems: 
            you might want to know the max amount you can rob up to a particular index multiple times
        optimal substructure:
            the max amount you can rob for the whole array relies on the max amount you can rob at each house.
        base cases:
            at house 0, the max you can rob is that number.
            at house 1, the max you can rob is the max of the 0th or 1st amounts;
        RECURRENCE RELATION:
            the max amount that i could rob up to and including this house is either:
                the max you could rob up to 2 houses ago + this house
                - or -
                just the amount you could rob at the previous house (and not including this house).
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]) 
        """
        memo = {}
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i - 2) + nums[i], dp(i - 1)) # recurrence relation
            return memo[i]
        
        return dp(len(nums) - 1)