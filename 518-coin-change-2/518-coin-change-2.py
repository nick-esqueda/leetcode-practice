class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        2D tab with coins as rows and amounts (amount all the way down to 0) as columns
        at each pos, set the pos in tab to the sum of two things:
        1. the value of the tab after you subtract the coin from the amount (amount - coin)
            - you'll look in the same row - tab[this coin row][amount - coin]
        2. the number if the row below in the same column
            - this is the number of combinations using the rest of the coins
        you'll start with a default row with all 0's
            - b/c there are 0 ways to get any amount with no coins to choose from
            
        ---
        you will have 0,1,2 for the cols, but obviously those are indices. need to key into the coins array with those indices
        ---
           0  1  2  3  4  5      
        1 [1, 1, 2, 2, 3, 4]
        2 [1, 0, 1, 0, 1, 1]
        5 [1, 0, 0, 0, 0, 1]
        """
        prev_coin_row = [0] * (amount + 1)
        
        for i in range(len(coins) - 1, -1, -1):
            coin = coins[i]
            row = [0] * (amount + 1) 
            row[0] = 1
            for amt in range(1, len(row)):
                combos = 0
                if amt - coin >= 0:
                    combos += row[amt - coin]
                combos += prev_coin_row[amt]
                row[amt] = combos
            prev_coin_row = row
            
        return prev_coin_row[-1]
    
    
    def change_TOPDOWN(self, amount: int, coins: List[int]) -> int:
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