def minimum_island(grid):
  """
  iterate through grid
  if you come across land, traverse
    get size
    mark all land as visited
  compare against/replace a running minimum
  """
  min_size = float('inf')
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 'L' and (r, c) not in visited:
        size = get_island_size(grid, r, c, visited)
        min_size = min(size, min_size)
  return min_size


def get_island_size(grid, r, c, visited):
  if r not in range(len(grid)) or c not in range(len(grid[0])):
    return 0
  if (r, c) in visited:
    return 0
  if grid[r][c] != 'L':
    return 0
  
  visited.add((r, c))
  size = 1
  size += get_island_size(grid, r - 1, c, visited)
  size += get_island_size(grid, r + 1, c, visited)
  size += get_island_size(grid, r, c - 1, visited)
  size += get_island_size(grid, r, c + 1, visited)
  return size
