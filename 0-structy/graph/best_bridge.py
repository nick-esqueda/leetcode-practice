from collections import deque

def best_bridge(grid):
  """
  traverse through first island you find and mark all L as visited
  starting from each L cell at once, BFS outwards
    neighbors will be W's or L's that are not in visited
    push nodes with distance tracker to q
    if you are looking at an L that is not in vis, return the associated distance 
      maybe -1 to get bridge length?
  """
  island_1 = find_island(grid)
  vis = set(island_1)
  q = deque([ (r, c, 0) for r, c in vis ])
  while q:
    (r, c, dist) = q.popleft()
    print(r, c, dist)
    
    if grid[r][c] == "L" and (r, c) not in island_1:
      return dist - 1
    
    for r, c in get_neighbors(grid, r, c):
      if (r, c) not in vis:
        vis.add((r, c))
        q.append((r, c, dist + 1))
  
  return "ERROR: no bridge determined"
      

def find_island(grid):
  vis = set()
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "L":
        mark_island(grid, r, c, vis)
        return vis
  return "ERROR: no island found"

  
def mark_island(grid, r, c, vis):
  if r not in range(len(grid)) or c not in range(len(grid[0])):
    return
  if grid[r][c] == "W":
    return
  if (r, c) in vis:
    return
  
  vis.add((r, c))
  mark_island(grid, r - 1, c, vis)
  mark_island(grid, r + 1, c, vis)
  mark_island(grid, r, c - 1, vis)
  mark_island(grid, r, c + 1, vis)
  
  
def get_neighbors(grid, r, c):
  neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
  def is_valid(coords):
    r, c = coords
    return r in range(len(grid)) and c in range(len(grid[0]))
  return list(filter(is_valid, neighbors))

  
grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
print(best_bridge(grid))
