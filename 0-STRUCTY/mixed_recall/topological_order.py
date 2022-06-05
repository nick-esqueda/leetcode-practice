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
  

def topological_order(graph):
  """
  map all nodes to parent counts
  for each node in graph, go through nei's and increment each of those nei's count in map
  get a collection of all nodes that are 'ready' (have 0 parents) [use deque]
  declare list for order
  while there are nodes in ready list: (len(graph)?)
    popleft
    add node to order
    decrement all of node's children in counts map
    if one of those children is now a 0, add it to the back of ready list
  return order
  """
  num_parents = {}
  for node in graph:
    num_parents[node] = 0
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1
        
  order = []
  ready = [node for node in num_parents if num_parents[node] == 0]
  while ready:
    cur = ready.pop()
    order.append(cur)
    for child in graph[cur]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)
        
  return order
  
  
print(topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
}))
