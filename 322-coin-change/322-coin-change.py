class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        find coin quantity for different amounts
        need 0 coins to get to an amount of 0
        for each amount after that (incrementing by 1):
            go through each coin in coins:
                subtract coin from the amount
                find that difference in the tab
                add 1 to the value of the tab at that difference
                    - this will be the amount of coins that it took to get to amount == 0
                reassign min coins variable accordingly
        """
        tab = [float('inf')] * (amount + 1)
        tab[0] = 0
        
        for amt in range(1, amount + 1):
            min_coins = float('inf')
            for coin in coins:
                attempt = amt - coin
                if attempt < 0 or tab[attempt] == float('inf'):
                    continue
                min_coins = min(1 + tab[attempt], min_coins)
            tab[amt] = min_coins
            
        return tab[amount] if tab[amount] != float('inf') else -1
        
        
    def coinChange_TOPDOWN(self, coins: List[int], amount: int) -> int:
        """
        decide to take each coin
        when the amount is 0, return 0
        add 1 to the return of each recursive call (since you took a coin)
        min value logic to find the least of each recursive call
        recurse for each choice of coin
        """
        memo = {}
        
        def min_change(amount):
            if amount in memo:
                return memo[amount]
            if amount <= 0:
                return amount

            min_count = float('inf')
            for coin in coins:
                count = 1 + min_change(amount - coin)
                if count > 0:
                    min_count = min(min_count, count)

            memo[amount] = min_count if min_count != float('inf') else -1
            return memo[amount]
        
        return min_change(amount)
                
