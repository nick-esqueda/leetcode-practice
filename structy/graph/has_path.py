from collections import deque

def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for nei in graph[src]:
    if (has_path(graph, nei, dst) is True):
      return True
  
  return False


def has_path(graph, src, dst):
  q = deque([src])
  while q:
    curr = q.popleft()
    if curr == dst:
      return True
    for nei in graph[curr]:
      q.append(nei)
  return False
