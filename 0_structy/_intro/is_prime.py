from math import ceil
def is_prime(n):
  """
  divide n by 2 to get a starting point
  for each number working down from the halfway point, if n is divisible by that num, return false
  if you've worked all the way down to 1, then you can exit and return true
  """
  if n == 1: return False
  for i in range(ceil(n / 2), 1, -1):
    if n % i == 0:
      return False
    
  return True
