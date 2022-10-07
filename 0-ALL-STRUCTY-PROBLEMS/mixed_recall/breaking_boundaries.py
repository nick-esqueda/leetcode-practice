def breaking_boundaries(m, n, k, r, c):
  return _breaking_boundaries(m, n, k, r, c, {})

def _breaking_boundaries(m, n, k, r, c, memo):
  """
  if r < m or c < n, return 1
  if k == 0, return 0
  can choose to go in any direction (and go back to where you came from)
  recurse for up down left right
  add up all of those recursive calls (they will return a number of ways for that position)
  when recursing, decrement k since you took up a move
  return the total number of ways
  """
  key = (k, r, c)
  if key in memo:
    return memo[key]
  if r not in range(m) or c not in range(n):
    return 1
  if k == 0:
    return 0
  
  num_ways = 0
  num_ways += _breaking_boundaries(m, n, k - 1, r - 1, c, memo)
  num_ways += _breaking_boundaries(m, n, k - 1, r + 1, c, memo)
  num_ways += _breaking_boundaries(m, n, k - 1, r, c - 1, memo)
  num_ways += _breaking_boundaries(m, n, k - 1, r, c + 1, memo)
  
  memo[key] = num_ways
  return memo[key]


print(breaking_boundaries(2, 2, 2, 1, 1) )
