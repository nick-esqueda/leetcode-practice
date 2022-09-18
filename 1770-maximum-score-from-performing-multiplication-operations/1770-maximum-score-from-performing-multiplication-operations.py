class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        dp(i, left) = max((mult[i] * nums[left]) + dp(i + 1, left + 1), (mult[i] * nums[left]) + dp(i + 1, left))
        """
        nums_len, mults_len = len(nums), len(multipliers)
        tab = [[0] * (mults_len + 1) for _ in range(mults_len + 1)] # must use 'm' for both lengths since left can only be as high as m.
        
        for i in range(mults_len - 1, -1, -1): # base case happens at i == m.
            for left in range(i, -1, -1): # left can only be as high as the number of multipliers used.
                mult = multipliers[i]
                right = (nums_len - 1) - (i - left)
                tab[i][left] = max((mult * nums[left]) + tab[i + 1][left + 1],
                                   (mult * nums[right]) + tab[i + 1][left])
        return tab[0][0]

        
        
    def maximumScore_TOPDOWN(self, nums: List[int], multipliers: List[int]) -> int:
        """
        PROBLEM:
        you will perform 1 operation with every index of multipliers, moving through the list. 
        must choose from either the start or the end of nums array, and then "remove it" once you use it.
        for whatever iteration you're on, you have to use multipliers at that 'i' to multiply with x, and then add that to running score.
        need to return the max score after going through the whole multipliers array.
        CHOICES - can choose to either take the first num in nums or the last num in nums.
        
        STATE:
        the current multipliers index - i (also means we've done 'i' operations so far).
        the left nums index, and the right nums index.
            we can use this to get the right index -> (n - 1) - (i - left)
            ^ this helps simplify the number of state variables and recurrence relation.
        
        SUBPROBLEMS:
        return the max possible score after already doing 'i' operations and using 'left' number of left nums.
        
        BASE CASES:
        if there are no multipliers, the max score would be 0.
        
        RECURRENCE RELATION:
        dp(i, left) = max((mult[i] * nums[left]) + dp(i + 1, left + 1), (mult[i] * nums[left]) + dp(i + 1, left))
        """
        # memo = {} # time constraints are too strict, so dict for stoarage will not be fast enough
        # def dp(i, left):
        #     key = (i, left)
        #     if i == len(multipliers):
        #         return 0
        #     if key not in memo:
        #         right = (len(nums) - 1) - (i - left)
        #         memo[key] = max((multipliers[i] * nums[left]) + dp(i + 1, left + 1),
        #                         (multipliers[i] * nums[right]) + dp(i + 1, left))
        #     return memo[key]
        
        @lru_cache(1000) # so memoization is faster
        def dp(i, left):
            if i == len(multipliers):
                return 0
            
            right = (len(nums) - 1) - (i - left)
            return max((multipliers[i] * nums[left]) + dp(i + 1, left + 1),
                       (multipliers[i] * nums[right]) + dp(i + 1, left))
        
        return dp(0, 0)