class Solution:
    def networkDelayTime(self, time: List[List[int]], n: int, k: int) -> int:
        k -= 1
        node_costs = [float('inf')] * n
        node_costs[k] = 0
        for _ in range(n - 1):
            changes = 0
            for node, nei, edge_cost in time:
                node, nei = node - 1, nei - 1 # to convert to 0 indexing
                
                if node_costs[node] + edge_cost < node_costs[nei]:
                    changes += 1
                    node_costs[nei] = node_costs[node] + edge_cost
            if not changes:
                break
                
        max_cost = 0
        for cost in node_costs:
            if cost == float('inf'):
                return -1
            max_cost = max(max_cost, cost)
        return max_cost
    
    
    def networkDelayTime_DIJKSTRA(self, times: List[List[int]], n: int, k: int) -> int:
        """
        [(src_node, target_node, time/weight), (src_node, target_node, time/weight), ...]
        need to construct adj list from times
        the node number will be the key of the adj list
        values will be a tuple of the time and the target node
        
        min heap, starting with the first node
        while the visited set is not as long as the number of nodes:
            pop from the heap
            go get all neighbors from the adjlist
            for each of those neighbors:
                if the cur neighbor hasn't been visited, add it to the heap
                when adding to heap, include the time PLUS the time that it took to get to the original node
        if you haven't visited all nodes, return -1
        
        ---
        if there is a cycle, what to do?
        if you just keep track of visited, you'd be able to not go back, and since you HAVE to start from k...
        ---
        we're not dealing with nodes that are connected to every single other node, we're just dealing with a DAG.
        since this is the case, we don't have to keep track of visited
        we also can just break out of the loop when the heap becomes empty
        the heap will only ever become empty once you've been to every node (i think?)
        """
        # adj = defaultdict(list)
        adj = { src: [] for src in range(1, n + 1) }
        for src, dst, time in times:
            adj[src].append((time, dst))
            
        max_time = 0
        vis = set()
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if node in vis:
                continue
            vis.add(node)
            max_time = max(max_time, time)
            for nei_time, nei_node in adj[node]:
                if nei_node not in vis:
                    heapq.heappush(heap, (time + nei_time, nei_node))
        return max_time if len(vis) == n else -1
                
        
        