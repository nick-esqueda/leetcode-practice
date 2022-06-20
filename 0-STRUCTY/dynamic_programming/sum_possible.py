def sum_possible(amount, numbers, memo={}):
  """
  if amount == 0, return True
  iterate through nums
    if amount - num < 0, continue to next iteration
    if amount - num > 0, call sum_possible(amount - num, numbers)
      if recursion returns true, return true
      otherwise, continue to next iteration
  if you go through all nums, return False
  """
  if amount in memo:
    return memo[amount]
  if amount < 0:
    return False
  if amount == 0:
    return True
  
  for num in numbers:
    if sum_possible(amount - num, numbers, memo):
      memo[amount] = True
      return True
      
  memo[amount] = False
  return False


# 2
def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  if amount < 0:
    return False
  if amount == 0:
    return True
  
  for num in numbers:
    if _sum_possible(amount - num, numbers, memo):
      memo[amount] = True
      return True
    
  memo[amount] = False
  return False
