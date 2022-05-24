from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  
  visited = { node_A }
  q = deque([ (node_A, 0) ]) # does this still need to be instantiated with list?
  while q:
    for i in range(len(q)):
      node, dist = q.popleft()
      
      if node == node_B:
        return dist
      
      for nei in graph[node]:
        if nei not in visited:
          visited.add(nei)
          q.append((nei, dist + 1))
    
  return -1


def build_graph(edges):
  graph = {}
  for a, b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph    
