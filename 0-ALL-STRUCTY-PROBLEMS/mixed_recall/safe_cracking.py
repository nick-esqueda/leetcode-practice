def safe_cracking(hints):
  graph = build_graph(hints)
  order = topological_order(graph)
  
  return ''.join(order)


def topological_order(graph):
  num_parents = {}
  for node in graph:
    num_parents[node] = 0
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1
      
  order = []
  ready = [node for node in num_parents if num_parents[node] == 0]
  while ready:
    node = ready.pop()
    order.append(str(node))
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)
        
  return order
  

def build_graph(edges):
  graph = {}
  for a, b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
  return graph

  
print(safe_cracking([
  (3, 1),
  (4, 7),
  (5, 9),
  (4, 3),
  (7, 3),
  (3, 5),
  (9, 1),
]))
