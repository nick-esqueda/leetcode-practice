class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if (r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[r]) or
                grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count