class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
        dijkstra SSSP
        """
        adj = { i: [] for i in range(n) }
        for i, edge in enumerate(edges):
            u, v = edge
            adj[u].append((succProb[i], v))
            adj[v].append((succProb[i], u))
        

        vis = set()
        pq = [(-1.0, start)] # want the max path - max heap instead of min heap
        while pq:
            wgt, node = heapq.heappop(pq)
            if node in vis:
                continue
            vis.add(node)
            
            if node == end:
                return -wgt
            
            for nei_wgt, nei in adj[node]:
                if nei not in vis:
                    heapq.heappush(pq, (-abs(nei_wgt * wgt), nei))
                    
        return 0