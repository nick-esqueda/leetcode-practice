class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        declare a current max var
        declare a vistied set
        iterate through every pos
        if pos == 1 and pos (coords) is not in the visited set...
          explore the island and return the size of that island
          if the size of the island is greater than curr max, replace
        return max area
        """
        def get_island_area(row, col):
          if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return 0
          if (row, col) in visited:
            return 0
          if grid[row][col] == 0:
            return 0
          
          visited.add((row, col))
          
          area = 1
          area += get_island_area(row - 1, col)
          area += get_island_area(row + 1, col)
          area += get_island_area(row, col - 1)
          area += get_island_area(row, col + 1)
          return area
        
        max_area = 0
        visited = set()
        for row in range(len(grid)):
          for col in range(len(grid[row])):
            if grid[row][col] == 1 and (row, col) not in visited:
              area = get_island_area(row, col)
              max_area = max(max_area, area)
        return max_area
        