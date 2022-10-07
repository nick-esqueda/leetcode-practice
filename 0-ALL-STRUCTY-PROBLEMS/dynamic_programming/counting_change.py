def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  """
  making decisions of "which coin to choose" leads to duplicate combinations/ways
    these combinations are the same combination but in a different order 
      ex. 1-1-2 and 1-2-1
  need to make decision of HOW MANY coins you want to take, then move on to the next coin
  
  whenever amount becomes 0, return up to caller and add 1 to a running way_count
    (if amount == 0: return 1)
  will the amount ever go negative, since your loop will only take the amount of coins
    that you can grab with change left over? how does the change get handled?
  
  instead of looping through coins and recursing for each coin, loop through 
  "quantity" of coins taken and recurse on each quantity, passing in a new coin
    need to stop looping when taking 'i' amount of coins makes the amount == 0
    iteration 0 will be 0 coins taken, meaning amount == amount
    iteration 1 will be 1 coin taken, meaning amount - 1*coin
    iteration 2 will be 2 coins taken, meaning amount - 2*coin
  toss in the 'coin_idx + 1' to recursive call each time you iterate. 
    this means that as you recurse downwards, each level of the recursive tree 
    will correspond to a new coin
  add the result of recursing to a running way_count
  return that way_count at the end of the function
  """
  key = (amount, i)
  if key in memo:
    return memo[key]
  if amount == 0:
    return 1
  if i == len(coins):
    return 0
  
  way_count = 0
  coin = coins[i] 
  for coin_qty in range((amount // coin) + 1):
    remainder = amount - (coin_qty * coin)
    way_count += _counting_change(remainder, coins, i + 1, memo)
    
  memo[key] = way_count
  return memo[key]
  
  
  
# 2 
def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]
  if amount == 0:
    return 1
  if i >= len(coins):
    return 0
  
  coin = coins[i]
  combos = 0
  for qty in range((amount // coin) + 1):
    combos += _counting_change(amount - (coin * qty), coins, i + 1, memo)
  
  memo[key] = combos
  return combos
    