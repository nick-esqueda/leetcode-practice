def largest_component(graph):
  largest = 0
  visited = set()
  for node in graph:
    if node not in visited:
      size = get_size(graph, node, visited)
      if size > largest:
        largest = size
  return largest


def get_size(graph, curr, visited):
  if curr in visited:
    return 0
  
  visited.add(curr)
  count = 1
  for nei in graph[curr]:
    count += get_size(graph, nei, visited)
  
  return count
  
