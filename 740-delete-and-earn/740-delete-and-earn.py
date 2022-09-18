class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        still need to have a counts map
        base cases:
            0 - the max points if 0 is the max in nums will be zero.
            1 - the max points if 1 is the max in nums will be however many 1's there are.
            
        dp[i] = max(dp[i - 1], points[i] + dp[i - 2])
        """
        M = max(nums)
        if M == 0:
            return 0    
        
        points = { i: 0 for i in range(M + 1) }
        for num in nums:
            # pre-calculate the number of points if you took every one of those point values.
            points[num] += num
            
        tab = [0] * (M + 1)
        tab[1] = points[1]
        
        for i in range(2, M + 1):
            tab[i] = max(tab[i - 1], points[i] + tab[i - 2])
        
        return tab[-1]
        
    
    def deleteAndEarn_TOPDOWN(self, nums: List[int]) -> int:
        """
        PROBLEM:
        want the max amount of points possible, but...
        must delete the current position to earn those points, THEN delete every num that is equal to that num + 1, and num - 1 (can maybe just ignore, instead of deleting).

        this problem sucks
        
        dp[i] = max(dp[i - 1], i*counts[i] + dp[i - 2])
        """
        max_num = max(nums)
        counts = { i: 0 for i in range(max_num + 1) }
        for num in nums:
            counts[num] += 1
        
        memo = {}
        def dp(i):
            if i <= 0:
                return 0
            if i not in memo:
                memo[i] = max(dp(i - 1), (i * counts[i]) + dp(i - 2))
            return memo[i]
        
        return dp(max_num)
            