class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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