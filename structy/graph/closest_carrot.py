from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  """
  BFS
  return dist if grid[r][c] == "C"
  only push neighs to queue if the are an O (or a C)
  ((r,c), dist)
  """
  vis = set()
  q = deque([ ((starting_row, starting_col), 0) ])
  while q:
    for _ in range(len(q)):
      coords, dist = q.popleft()
      r, c = coords
      
      if grid[r][c] == "C":
        return dist
      
      neighbors = get_neighbors(grid, r, c)
      for nei in neighbors:
        if nei not in vis:
          # nei looks like: (r, c)
          vis.add(nei)
          q.append((nei, dist + 1))
          
  return -1
      
  
def get_neighbors(grid, r, c):
  neighbors = [
    (r - 1, c),
    (r + 1, c),
    (r, c - 1),
    (r, c + 1)
  ]
  
  def is_nei_valid(nei):
    r, c = nei
    is_in_bounds = r in range(len(grid)) and c in range(len(grid[0]))
    if is_in_bounds:
      is_open_space = grid[r][c] == "O" or grid[r][c] == "C"
      return is_open_space and is_in_bounds
    return False
  
  return list(filter(is_nei_valid, neighbors))

# grid = [
#   ['O', 'O', 'O', 'O', 'O'],
#   ['O', 'X', 'O', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['O', 'X', 'C', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['C', 'O', 'O', 'O', 'O'],
# ]
# print(get_neighbors(grid, 1, 2))
