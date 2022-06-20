def min_change(amount, coins, memo={}):
  """
  if amount is < 0, return -1
  if amount is 0, return 0
  
  curr_min = float('inf')
  for coins in coins...
    find min_change(amount - coin)
      [if amount ends up being negative, base case out]
      if that call returns a positive number or 0, set curr_min appropriately
        [don't add 1 yet, since you're just checking the amount of coins for each child call]
  after looping, return -1 if curr_min is not an int, otherwise curr_min + 1
    (because you never found a combination that will create the amount)
    (+ 1 is to count this stack frame as a coin required to make total)
  """
  if amount in memo:
    return memo[amount]
  if amount < 0:
    return -1
  if amount == 0:
    return 0
  
  curr_min = float("inf")
  
  for coin in coins:
    num_coins = min_change(amount - coin, coins)
    if num_coins >= 0:
      curr_min = min(num_coins, curr_min)
    
  memo[amount] = curr_min + 1 if isinstance(curr_min, int) else -1
  return memo[amount]
    
    
# 2
def min_change(amount, coins):
  return _min_change(amount, coins, {})

def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]
  if amount == 0:
    return 0
  if amount < 0:
    return -1
  
  min_coins = float('inf')
  for coin in coins:
    count = _min_change(amount - coin, coins, memo)
    if count >= 0:
      min_coins = min(count + 1, min_coins)
  
  memo[amount] = -1 if min_coins == float('inf') else min_coins
  return memo[amount]
