class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      """
      same as course sched 1, but push courses to an array before returning true at end of dfs
      
      create adj list
      
      declare order = []
      for each course in adj list, traverse starting at course with new set() every time
        if the traversal returns False, early return -> [] from whole func
      return order
      
      traversal:
        if the course has no prereqs, return true
        if the course is in visited set already, return false
        add the course to visited
        for each prereq:
          if trav() returns false, early return false
        if you haven't returned yet...
        set courses prereqs to [] in adj list
        push this course to the order list
        return True
      """
      
      graph = {}
      for course, prereq in prerequisites:
        if course not in graph: graph[course] = []
        if prereq not in graph: graph[prereq] = []
        graph[course].append(prereq)
        
      def can_finish(course, visited):
        if graph[course] == []:
          if course not in order:
            order.append(course)
          return True
        if course in visited:
          return False
        
        visited.add(course)
        for prereq in graph[course]:
          if not can_finish(prereq, visited):
            return False
        
        graph[course] = []
        order.append(course)
        return True
      
      order = []
      for course in graph:
        if not can_finish(course, set()):
          return []
        
      for i in range(numCourses):
        if i not in order:
          order.append(i)
        
      return order
        
        
