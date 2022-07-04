class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        bottom right has a min of whatever num is in that pos
        at each pos, take the min of right and bottom, and set that pos to that min + pos
        """
        tab = [float('inf')] * (len(grid[0]) + 1)
        
        for r in range(len(grid) - 1, -1, -1):
            row = [float('inf')] * (len(grid[0]) + 1)
            for c in range(len(grid[0]) - 1, -1, -1):
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    row[c] = grid[r][c]
                    continue
                row[c] = grid[r][c] + min(row[c + 1], tab[c])
            tab = row
        return tab[0]
        