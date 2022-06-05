class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      """
      topological order
      *need to account for cycles
      *need to handle courses that don't have prerequisites
      """
      graph = self.create_graph(prerequisites, numCourses)
        
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
        order.append(node)
        for child in graph[node]:
          num_parents[child] -= 1
          if num_parents[child] == 0:
            ready.append(child)
            
      for node in num_parents:
        if num_parents[node] > 0:
          return []
        
      return order[::-1]
        
    def create_graph(self, edges, numCourses):
      graph = { i: [] for i in range(numCourses) }
      for course, prereq in edges:
        if course not in graph:
          graph[course] = []
        if prereq not in graph:
          graph[prereq] = []
        graph[course].append(prereq)
      return graph
