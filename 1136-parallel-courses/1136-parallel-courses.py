class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        start at the nodes with 0 parents, and with each level, increment a semester count
        modified kahn's algorithm
        if the number of nodes you've seen after traversing is less than the amount of nodes in the graph, you had a cycle
        this is because you will only push nodes on to the queue if they have 0 parents left. a cycle node will always have another parent that you can't get to
        """
        
        adj = { i: [] for i in range(1, n + 1) }
        in_degree = [0] * (n + 1)
        for a, b in relations:
            adj[a].append(b)
            in_degree[b] += 1
            
        q = deque()
        for course in adj:
            if in_degree[course] == 0:
                q.append(course)
               
        sems = 0
        vis = set()
        while q:
            sems += 1
            for _ in range(len(q)):
                course = q.popleft()
                vis.add(course)
                for child in adj[course]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        q.append(child)
            
        return sems if len(vis) == n else -1
            
        
        
