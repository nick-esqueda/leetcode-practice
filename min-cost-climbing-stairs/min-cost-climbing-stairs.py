class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        loop backwards to start at the base cases
        recurrence relation:
            the min cost to the top from here is this cost + the cheaper of the min costs for the next two steps
            (work backwards)
            dp[i] = costs[i] + min(dp[i + 1], dp[i + 2])
        """
        if len(cost) == 1:
            return cost[0]
        
        tab = [float('inf')] * len(cost)
        tab[-1], tab[-2] = cost[-1], cost[-2]
        
        for i in range(len(cost) - 3, -1, -1):
            tab[i] = cost[i] + min(tab[i + 1], tab[i + 2])
        return min(tab[0], tab[1])
        
    
    def minCostClimbingStairs_TOPDOWN(self, cost: List[int]) -> int:
        """
        PROBLEM:
            minumum cost to reach 1 step out of bounds
            once you pay the cost at i, you can move forward either 1 or 2 steps
            you can start at either the 0th or 1st index
        subproblems:
            the min cost to the top at index 0 relies on the min cost at idx 1 and idx 2, etc...
        overlapping subproblems:
            the min cost for step 3 might be needed for step 1 and 2, etc...
        optimal substructure:
            the optimal solution to 2 different steps are needed to calculate the main solution.
        DP!
        base cases:
            at the last index, the min cost to reach the top is the cost at that index
            at the second to last index, the min cost is the cost at that index as well
        recurrence relation:
            the min cost to the top from here is this cost + the cheaper of the min costs for the next two steps
            (work backwards)
            dp[i] = costs[i] + min(dp[i + 1], dp[i + 2])
        state variables:
            i (index inside the cost array)
        """
        memo = {}
        def dp(i):
            if i == len(cost) - 1 or i == len(cost) - 2:
                return cost[i]
            if i not in memo:
                memo[i] = cost[i] + min(dp(i + 1), dp(i + 2))
            return memo[i]
        
        return min(dp(0), dp(1))