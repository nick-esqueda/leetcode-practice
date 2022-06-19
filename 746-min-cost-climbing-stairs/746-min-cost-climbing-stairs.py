class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        """
        memo = {}
        def get_min(i):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            
            curr_cost = cost[i]
            memo[i] = curr_cost + min(get_min(i + 1), get_min(i + 2))
            return memo[i]
        
        return min(get_min(0), get_min(1))
            