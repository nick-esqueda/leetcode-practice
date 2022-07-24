class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        if you perform a dfs on every single node (including visited nodes), you can add the starting node of the dfs to the ancestor list of each child node
        """
        adj = { i: [] for i in range(n) }
        for a, b in edges:
            adj[a].append(b)
            
        def get_ancestors(node, start):
            if not (ancestors[node] and ancestors[node][-1] == start):
                if node != start:
                    ancestors[node].append(start)
                
                for child in adj[node]:
                    get_ancestors(child, start)
            
        ancestors = [[] for _ in range(n)]    
        for node in range(n):
            get_ancestors(node, node)
        
        return ancestors


    def getAncestors_KAHNS(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        add the current node into the ancestor list for each child
        make sure that you process the least value parent first
        """
        adj = { i: [] for i in range(n) }
        in_count = [0] * n
        for parent, child in edges:
            adj[parent].append(child)
            in_count[child] += 1
            
        ancestors = [set() for _ in range(n)] # each index i represents the i'th node, and the array in that index represents all of the ancestors of that node
        q = deque([ c for c in adj if in_count[c] == 0 ])
        while q:
            parent = q.popleft()
            for child in adj[parent]:
                ancestors[child].add(parent)
                ancestors[child].update(ancestors[parent])
                in_count[child] -= 1
                if in_count[child] == 0:
                    q.append(child)
            
        return [sorted(anc) for anc in ancestors]
        