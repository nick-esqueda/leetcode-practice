class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows, num_cols = len(heights), len(heights[0])
        
        def dfs(r, c, vis, matrix, prev_height=float('-inf')):
            pos = (r, c)
            if (r < 0 or r == num_rows or
                c < 0 or c == num_cols or
                pos in vis):
                return
            
            height = matrix[r][c]
            if height < prev_height:
                return
            
            vis.add(pos)
            dfs(r - 1, c, vis, matrix, height)
            dfs(r + 1, c, vis, matrix, height)
            dfs(r, c - 1, vis, matrix, height)
            dfs(r, c + 1, vis, matrix, height)
        
        
        pacific, atlantic = set(), set()
        for r in range(num_rows):
            dfs(r, 0, pacific, heights)
            dfs(r, num_cols - 1, atlantic, heights)
        for c in range(num_cols):
            dfs(0, c, pacific, heights)
            dfs(num_rows - 1, c, atlantic, heights)
            
        return pacific & atlantic