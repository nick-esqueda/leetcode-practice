def has_cycle(graph):
  """
  """
  black = set()
  for node in graph:
    if find_cycle(graph, node, set(), black):
      return True
  return False

def find_cycle(graph, node, grey, black):
  if node in grey:
    return True
  if node in black:
    return False
  
  grey.add(node)
  for nei in graph[node]:
    if find_cycle(graph, nei, grey, black) is True:
      return True
    
  grey.remove(node)
  black.add(node)
  return False
  
