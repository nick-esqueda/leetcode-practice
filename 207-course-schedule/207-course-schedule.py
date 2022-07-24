class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        the only way you cannot finish the courses is if there is a cycle
        build the adj list
        dfs over every node with a path and processed set - if you come across a node in the path set, there's a cycle
        """
        
        adj = { i: [] for i in range(numCourses) }
        for a, b in prerequisites:
            adj[a].append(b)
            
            
        def detect_cycle(node: int, path: set) -> bool:
            if node in done:
                return False
            if node in path:
                return True
            
            path.add(node)
            for nei in adj[node]:
                if detect_cycle(nei, path):
                    return True
            path.remove(node)
            done.add(node)
            
        done = set()
        for course in adj:
            if detect_cycle(course, set()):
                return False
        return True
        