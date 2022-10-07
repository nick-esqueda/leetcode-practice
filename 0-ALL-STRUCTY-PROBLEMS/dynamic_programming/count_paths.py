def count_paths(grid, r=0, c=0, memo={}):
  """
  if the r or c is out of bounds, return 0
  if the curr pos is the bottom right, return 1
  if the grid at curr pos is an X, return 0
  the num of paths from any pos is the num of paths from the right pos + down pos
  """
  if (r, c) in memo:
    return memo[(r, c)]
  if r not in range(len(grid)) or c not in range(len(grid[0])):
    return 0
  if grid[r][c] == "X":
    return 0
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return 1
  
  down_count = count_paths(grid, r + 1, c)
  right_count = count_paths(grid, r, c + 1)
  memo[(r, c)] = down_count + right_count
  return memo[(r, c)]


# 2 
def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
  key = (r, c)
  if key in memo:
    return memo[key]
  if r >= len(grid) or c >= len(grid[0]):
    return 0    
  if grid[r][c] == "X":
    return 0
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return 1
  
  memo[key] = _count_paths(grid, r + 1, c, memo) + _count_paths(grid, r, c + 1, memo)
  return memo[key]
