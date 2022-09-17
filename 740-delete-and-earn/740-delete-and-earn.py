class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
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
            