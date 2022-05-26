def longest_path(graph):
  """
  create hashmap to associate nodes with their distance from a dead end
  loop thorugh graph and put all dead ends with a dist of 0 into map
  traverse starting at each node in the graph
    if you come across a node that is already in the dist map, return that value
    store node with 1 + traverse() in the distance map
  now that you have all distances, return the max of dist map's values
  """
  distances = {}
  for node in graph:
    if graph[node] == []:
      distances[node] = 0
  
  max_dist = 0
  for node in graph:
    max_dist = max(get_distances(graph, node, distances), max_dist)
    
  return max_dist
  

def get_distances(graph, node, distances):
  if node in distances:
    return distances[node]
  
  dist = 1
  for nei in graph[node]:
    dist = max(get_distances(graph, nei, distances) + 1, dist)
    
  distances[node] = dist
  return dist
