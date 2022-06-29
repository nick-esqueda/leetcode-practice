class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        just need to take the least neighbor and traverse through the grid, always going along the path that costs the least
        if you didn't take the path that cost the least, that means that you'd be sitting there waiting for water to rise irl
        always track which node had the greatest weight to travel to, since that's how long you would need to wait
            for the water to rise (remember you can swim at infinite speed)
        once you get to the bottom right, go ahead and return the max weight after you've taken that weight into account
            
        nodes will be: (value at grid (weight), r, c)
        """
        max_height = 0
        vis = set()
        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)
        while heap:
            height, r, c = heapq.heappop(heap)
            pos = (r, c)
            if pos in vis:
                continue
                
            vis.add(pos)
            max_height = max(max_height, height)
            if r == len(grid) - 1 and c == len(grid) - 1:
                return max_height
            
            neis = self.get_neighbors(grid, r, c)
            for nei in neis:
                nr, nc = nei
                if nei not in vis:
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
        
    def get_neighbors(self, grid, r, c):
        possible_neis = [
            [r - 1, c],
            [r + 1, c],
            [r, c + 1],
            [r, c - 1],
        ]
        
        def is_valid(r, c):
            return r in range(len(grid)) and c in range(len(grid[0]))
    
        return [(r, c) for r, c in possible_neis if is_valid(r, c)]