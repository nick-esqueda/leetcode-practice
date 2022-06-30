class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        the "top" is the other side of the end of the array visually, [1, 2, 3][top]
        the min cost to get to the top at the very last position is the cost at that position
        the min cost to get to the top at the top is 0
        BOTTOM UP:
        work backwards step by step and calculate the min cost of going forward either one or two steps
        make sure to add yourself to that sum, and that will be the min cost from that position
        once you're done iterating, take the min of the costs at the first two positions
        """
        i = len(cost) - 3
        while i >= 0:
            cur_price = cost[i]
            cost[i] = min(cur_price + cost[i + 1], cur_price + cost[i + 2])
            i -= 1
        return min(cost[0], cost[1])
    
    
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         """
#         """
#         memo = {}
#         def get_min(i):
#             if i in memo:
#                 return memo[i]
#             if i >= len(cost):
#                 return 0
            
#             curr_cost = cost[i]
#             memo[i] = curr_cost + min(get_min(i + 1), get_min(i + 2))
#             return memo[i]
        
#         return min(get_min(0), get_min(1))
            