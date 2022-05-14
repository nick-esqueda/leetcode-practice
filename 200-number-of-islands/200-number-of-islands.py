class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        declare a count var
        declare a visited set
        iterate through every pos
        if the pos is a 1 and hasn't been visited yet, DFT through that island, marking all spots as visited
        once you're done traversing, increment the count var
        keep iterating through pos's and repeat ^
        return count at the end
        """
        def explore(row, col):
          if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return
          if grid[row][col] == "0":
            return
          if (row, col) in visited:
            return
      
          visited.add((row, col))
          explore(row - 1, col)
          explore(row + 1, col)
          explore(row, col - 1)
          explore(row, col + 1)
          return
          
        count = 0
        visited = set()
        for i in range(len(grid)):
          for j in range(len(grid[i])):
            if grid[i][j] == "1" and (i, j) not in visited:
              explore(i, j)
              count += 1
        return count
          