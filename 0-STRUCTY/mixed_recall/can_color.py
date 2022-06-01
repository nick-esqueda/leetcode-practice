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
    


def can_color(graph):
  colors = {}
  for node in graph:
    if node not in colors:
      if color(node, graph, colors, True) is False:
        return False
  
  return True
  
def color(node, graph, colors, desired_color):
  """
  if the node is in colors:
    return desired_colors == colors[node]
  paint each node the desired_color
  for each nei:
    color() those neis
    if color comes back False at any point, return False
  if you go through all neighbors and don't return F, return T
  """
  if node in colors:
    return desired_color == colors[node]
  
  colors[node] = desired_color
  
  for nei in graph[node]:
    if color(nei, graph, colors, not desired_color) is False:
      return False
    
  return True
    
  