def topological_order(graph):
  """
  visit all neighbors first
  once you are done visiting neis, push node to arr
  don't visit visited neis
  """
  order = []
  visited = set()
  for node in graph:
    if node not in visited:
      explore(graph, node, visited, order)
  return order[::-1]
  
def explore(graph, node, visited, order):
  if node in visited:
    return
  
  visited.add(node)
  for nei in graph[node]:
    explore(graph, nei, visited, order)
    
  order.append(node)
  
