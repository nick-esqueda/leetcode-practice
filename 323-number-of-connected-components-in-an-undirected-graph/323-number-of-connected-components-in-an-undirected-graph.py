class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        build an adj list from the edges
        perform a dfs over each unvisited node, incrementing the count each time you move on to a new component
        """
        adj = { i: [] for i in range(n) }
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        def dfs(node):
            if node in vis:
                return
            
            vis.add(node)
            for nei in adj[node]:
                dfs(nei)
            
        count = 0
        vis = set()
        for node in adj:
            if node not in vis:
                dfs(node)
                count += 1
        return count
