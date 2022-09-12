class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        number of ways - DP
        topdown memoization, returning 1 for each new way and 0 if not a way
        """
        
        memo = {}
        def get_ways(i, total):
            key = (i, total)
            if key in memo:
                return memo[key]
            if i >= len(nums):
                return 1 if total == target else 0
            
            ways = (get_ways(i + 1, total + nums[i]) + 
                    get_ways(i + 1, total - nums[i]))
            memo[key] = ways
            return ways
        
        return get_ways(0, 0)