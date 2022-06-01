def can_color(graph):
  """
  put alternating nodes in a black or white set
  
  loop through all nodes in graph
    if any of the neighbors of that node are in the same set as node, return False
  return True if you go through all nodes and don't find any neighboring colors
  """
  black = set()
  white = set()
  
  for node in graph:
    color_nodes(node, graph, black, white, 'black')
    
    color = black if node in black else white
    for nei in graph[node]:
      if nei in color:
        return False
  
  return True
        
  
def color_nodes(node, graph, black, white, choice):
  if node in black or node in white:
    return
  
  if choice == 'black':
    black.add(node)
    for nei in graph[node]:
      color_nodes(nei, graph, black, white, 'white')
  elif choice == 'white':
    white.add(node)
    for nei in graph[node]:
      color_nodes(nei, graph, black, white, 'black')
    
