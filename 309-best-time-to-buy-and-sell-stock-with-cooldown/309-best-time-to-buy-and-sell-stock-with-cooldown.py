class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        you can decide to buy or hold
        if you buy, you can sell or hold
        you can only sell after you've bought
        you cannot buy again until after you've sold
        need to get the max path of all of these decisions
        """
        memo = {}
        def backtrack(i, bought):
            key = (i, bought)
            if key in memo:
                return memo[key]
            if i >= len(prices):
                return 0
            
            price = prices[i]
            if not bought:
                hold = backtrack(i + 1, False)
                buy = backtrack(i + 1, True) - price
                memo[key] = max(hold, buy)
                return memo[key]
            elif bought:
                hold = backtrack(i + 1, True)
                sell = price + backtrack(i + 2, False)
                memo[key] = max(hold, sell) 
                return memo[key]
            
        
        return backtrack(0, False)