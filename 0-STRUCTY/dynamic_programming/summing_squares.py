def summing_squares(n):
  """
  calculate and return all perfect squares that are less than n
  feed n and a list of those squares to min_squares
  """
  squares = [ i*i for i in range(1, n + 1) if i*i <= n ]
  return min_squares(n, squares, {})


def min_squares(n, squares, memo):
  """
  if n < 0, return float('inf')
  if n == 0, return 1
  declare running min
  iterate over squares
    subtract curr square from n and pass into min_squares
    if the result of min_squares < min, reassign
    
  return min + 1 
    (+ 1 is for our current frame)
  """
  if n in memo:
    return memo[n]
  if n == 0:
    return 0
  
  curr_min = float('inf')
  for square in squares:
    if n - square >= 0:
      num_squares = 1 + min_squares(n - square, squares, memo)
      curr_min = min(num_squares, curr_min)
    
  memo[n] = curr_min
  return memo[n]
  
  
