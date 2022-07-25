class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        dijkstra
        the edge weight to a neighbor node will be the nei's cell value minus the current cell value
        since you will always choose to expand the node with the best cost, you can just keep track of a max of all of those edge costs
            but ONLY if it is in the final path
            
        dijkstra will give you the length of the shortest path, and maybe also the path
        but you don't want the shortest path, you want the path that has the smallest effort
        if dijkstra gets to a node that has a higher weight, it will only go back to that edge if all other edges are also that same weight or greater
            this is because the heap will always have the edge with minimum weight (effort) at the top of it
        knowing this, this means that you can always check for a max of the minimum effort while working towards the bottom right cell
        but you have to make sure that you are on the final path before you take those maxes into account...
        if you make sure to return once you get to the bottom right, then you know for certain that the only edges that were taken into the max calculation were the smallest ones
        """
        most_effort = float('-inf')
        vis = set()
        pq = [(0, 0, 0)]
        while pq:
            effort, r, c = heapq.heappop(pq)
            if (r, c) in vis:
                continue
            
            vis.add((r, c))
            most_effort = max(most_effort, effort)
            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                return most_effort
            
            neis = self.get_neighbors(heights, r, c)
            for nr, nc in neis:
                if (nr, nc) not in vis:
                    nei_effort = abs(heights[nr][nc] - heights[r][c])
                    heapq.heappush(pq, (nei_effort, nr, nc))
        
    
    def get_neighbors(self, matrix, r, c):
        neis = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        def is_valid(coord):
            return coord[0] in range(len(matrix)) and coord[1] in range(len(matrix[0]))
        return [nei for nei in neis if is_valid(nei)]
            
            
