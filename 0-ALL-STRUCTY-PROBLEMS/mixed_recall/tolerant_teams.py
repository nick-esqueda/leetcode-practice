def tolerant_teams(rivalries):
  """
  make a graph with the given rivalries/undirected edges
  for each person/node:
    traverse() and color the graph if the node hasn't been colored yet
    if the traversal returns False, return False
  when you color the whole graph without returning False, return True
  """ 
  graph = create_graph(rivalries)
  
  teams = {}
  for person in graph:
    if person not in teams:
      if not create_teams(person, graph, teams, True):
        return False
  
  return True


def create_teams(person, graph, teams, desired_team):
  """
  if person is in teams, return teams[person] == desired_team
  put that person the desired team if not yet there
  for each neighbor in the graph:
    if create_team returns False at any point, return False
  after making it through the loop, return True
  """
  if person in teams:
    return teams[person] == desired_team
  
  teams[person] = desired_team
  
  for nei in graph[person]:
    if not create_teams(nei, graph, teams, not desired_team):
      return False
    
  return True
  
    
def create_graph(edges):
  graph = {}
  for r1, r2 in edges:
    if r1 not in graph:
      graph[r1] = []
    if r2 not in graph:
      graph[r2] = []
    graph[r1].append(r2)
    graph[r2].append(r1)
  
  return graph


print(tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader'),
  ('raj', 'philip'),
  ('seb', 'raj')
]) )
