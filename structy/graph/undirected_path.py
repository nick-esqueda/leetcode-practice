def undirected_path(edges, node_A, node_B):
  graph = convert_to_graph(edges)
  return find_node(graph, node_A, node_B, set())
  

def find_node(graph, node_A, node_B, visited):
  if node_A in visited:
    return False
  if node_A == node_B:
    return True
  
  visited.add(node_A)
  for nei in graph[node_A]:
    if (find_node(graph, nei, node_B, visited) is True):
      return True
    
  return False
  
  
def convert_to_graph(edges):
  graph = {}
  for a, b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
    
  return graph
