def island_count(grid):
  """
  iterate through grid
  traverse each island and mark nodes as visited
  increment count after each traversal
  """
  count = 0
  visited = set()
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if (row, col) not in visited and grid[row][col] == "L":
        explore(grid, row, col, visited)
        count += 1
        
  return count

def explore(grid, row, col, visited):
  if row not in range(len(grid)) or col not in range(len(grid[0])):
    return
  if (row, col) in visited:
    return
  if grid[row][col] != "L":
    return
  
  visited.add((row, col))
  explore(grid, row + 1, col, visited)
  explore(grid, row - 1, col, visited)
  explore(grid, row, col + 1, visited)
  explore(grid, row, col - 1, visited)
