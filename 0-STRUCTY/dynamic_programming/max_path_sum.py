def max_path_sum(grid, r=0, c=0, memo={}):
  """
  if curr pos is out of bounds, return 0
  if r,c is the bottom right, return the value at that pos
  
  pos's max path sum =
    take the max of the right and down paths, and add curr pos's value to that
  """
  pos = (r, c)
  if pos in memo:
    return memo[pos]
  if r not in range(len(grid)) or c not in range(len(grid[0])):
    return 0
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return grid[r][c]
  
  memo[pos] = (
    max(max_path_sum(grid, r + 1, c, memo), max_path_sum(grid, r, c + 1, memo))
        + grid[r][c]
  )
  return memo[pos]


# 2
def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, r, c, memo):
  key = (r, c)
  if key in memo:
    return memo[key]
  if r >= len(grid) or c >= len(grid[0]):
    return 0
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return grid[r][c]
  
  memo[key] = grid[r][c] + max(
    _max_path_sum(grid, r + 1, c, memo), 
    _max_path_sum(grid, r, c + 1, memo))
  return memo[key]
