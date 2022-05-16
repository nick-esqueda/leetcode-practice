class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        create adj list from prereqs
        declare can_finish var = True
        for each course in adj list, IF that course has prereqs, perform a DFS to see if canFinish
          (pass in a new visited set on each call)
          if any call returns false, return False from whole func
        at very end, return True
        
        DFS:
          if the course is already in the visited set, return false
          add course to visited set
          for each neighbor/prereq
            if not canFinish, return false
          set prereq list to empty if you haven't returned false yet
          return true at end of func (this means that you canFinish all courses leading up to this course)
        
        ???:
        if we start at 0/the first course, will we always be able to tell from that node if we can take every course?
        """
        graph = {}
        for course, prereq in prerequisites:
          if course not in graph: graph[course] = []
          if prereq not in graph: graph[prereq] = []
          graph[course].append(prereq)
          
          
        def dft(course, visited):
          if graph[course] == []:
            return True
          if course in visited:
            print(course, 'here')
            return False
          
          visited.add(course)
          for prereq in graph[course]:
            if dft(prereq, visited) is False:
              return False
          
          graph[course] = []
          return True
          
          
        for course in graph:
          if graph[course]:
            print ('course adhakdsjjadsf', course)
            if dft(course, set()) is False:
              return False
            
        return True
            
          
