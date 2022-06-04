def string_search(grid, s):
  """
  iterate through each pos until you find s[0]
  once you do, start off a search
  if the search comes back False keep iterating
  otherwise, return True
  if you visited every pos with no luck, return False
  """
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == s[0] and (r, c) not in visited:
        if search(grid, r, c, s, 0, visited) is True:
          return True
  return False
        
      

def search(grid, r, c, s, i, visited):
  """
  if the r or c are out of bounds, return False
  if (r,c) in visited, return False
  if the letter at pos is not s[i], return False
  if letter at pos == s[-1], return True
  search() all up down left right nei's, incrementing i
  if any of those searches return True, return True
  if go through all nei's with no True, return False
  """
  if r not in range(len(grid)) or c not in range(len(grid[0])):
    return False
  if (r, c) in visited:
    return False
  if grid[r][c] != s[i]:
    return False
  
  if grid[r][c] == s[-1] and i == len(s) - 1:
    return True
  
  visited.add((r, c))
  deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for dr, dc in deltas:
    nei_r = r + dr
    nei_c = c + dc
    if search(grid, nei_r, nei_c, s, i + 1, visited):
      return True
    
  return False
    
  
