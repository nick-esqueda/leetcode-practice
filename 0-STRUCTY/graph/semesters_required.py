from collections import deque

def semesters_required(num_courses, prereqs):
  """
  longest path
  mark all courses with no prereqs as dead ends (dist as 1)
    try doing this in the recursive func
  iterate through all courses
    recurse to collect length starting from course
    if the length is greater than curr max, replace
  return the longest path
  """
  graph = { i: [] for i in range(num_courses) }
  for a, b in prereqs:
    graph[a].append(b)
    
  sems_reqd = {}
  longest = 0
  for course in graph:
    if course not in sems_reqd:
      longest = max(get_sems_reqd(graph, course, sems_reqd), longest)
    
  return longest


def get_sems_reqd(graph, course, sems_reqd):
  if graph[course] == []:
    sems_reqd[course] = 1
  if course in sems_reqd:
    return sems_reqd[course]
  
  sems = 2
  for prereq in graph[course]:
    prereqs_sems = get_sems_reqd(graph, prereq, sems_reqd)
    sems = max(prereqs_sems + 1, sems)
    
  sems_reqd[course] = sems
  return sems

  