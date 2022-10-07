def rare_routing(n, roads):
  """
  create a graph from roads
  traverse through nodes, passing in a visited set
  if the traversal returns False, return False
  if the amount of visited nodes is not equal to n, that means you have multiple components
    which also means that you have 2 cities that DON'T have a path between them, which is bad
  return True if len(visited) == n else False
  """
  graph = create_graph(roads)
  visited = set()
  if not has_unique_routes(0, graph, visited):
    return False
  
  return len(visited) == n
  
  
def has_unique_routes(node, graph, visited, prev=None):
  """
  need to visit every city, without backtracking to a city
  if node in visited, return False
  put the current node in visited
  for every neighbor:
    if the neighbor is NOT prev, then you can...
      check if has_unique_routes
      if returns False at any point, return False for this call
  after making it through all neighbors, return True
  """
  if node in visited:
    return False
  
  visited.add(node)
  for nei in graph[node]:
    if nei != prev and not has_unique_routes(nei, graph, visited, node):
      return False
    
  return True


def create_graph(edges):
  graph = {}
  for a, b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
      
  return graph


print(rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3)
]))
