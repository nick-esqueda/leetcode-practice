class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        you have an array of point coords [[x, y], [x, y]]
        
        set up a heap initialized with the first point in the graph
        pop from the heap to get the current node 
        print node
        if this node is not already in visited:
            increment the total cost var
            calculate the weight to all of the other nodes and store inside tuple with node
            add all of those neighbors/weights to the heap
            
        TRY NOT STARTING AT I + 1 TO SEE IF TIMEOUT
        """
        adj = { i: [] for i in range(len(points)) }
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
                
        min_cost = 0
        heap = [(0, 0)]
        heapq.heapify(heap)
        vis = set()
        while len(vis) < len(points):
            weight, coord_idx = heapq.heappop(heap)
            
            if coord_idx not in vis:
                min_cost += weight
                vis.add(coord_idx)
                for nei in adj[coord_idx]:
                    heapq.heappush(heap, nei)
                    
        return min_cost
        
