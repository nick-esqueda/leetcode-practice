class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        making the decision of what coin to choose will end up with multiple permutations of the same answer
            - b/c you are able to revisit a coin you've already used in the past
        what you can instead do is choose the quantity of each coin that you want to use
        that way, on each level of the decision tree, you're making a choice for one coin, and not revisiting a coin
        once you hit amount = 0, can return 1 since you found a combination
        loop through the different quanitities that you can take of the coin
        you can only take as many coins that don't go over amount
        
        amt=16 coin=5 0 1 2 3
        """
        memo = {}
        def find_change(i, amount):
            key = (i, amount)
            if key in memo:
                return memo[key]
            if amount == 0:
                return 1
            if i >= len(coins):
                return 0
            
            coin = coins[i]
            combos = 0
            for qty in range((amount // coin) + 1):
                combos += find_change(i + 1, amount - (coin * qty))
            memo[key] = combos
            return combos
        
        return find_change(0, amount)