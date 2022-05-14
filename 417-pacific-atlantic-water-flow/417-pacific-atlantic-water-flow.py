class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        declare pac_set and atl_set
        explore() starting from cells touching the pac, and mark cells that can get to pac in pac_set
        ^ do the same but starting from cells touching the atl, but push to atl_set
        return whichever coords are in both sets
        
        explore()
          if the cell is out of bounds, return
          if the cell is in ONLY the corresponding set, return
          mark the cell inside of corresponding set
          if the top cell's val >= curr cell's val, explore the top cell
            (do the same for bottom left right)
          return nothing at end (only traversing to collect cell coords)
        """
        def explore(row, col, visited, prev_height):
          if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]):
            return
          if heights[row][col] < prev_height:
            return
          if (row,col) in visited:
            return
          
          visited.add((row,col))
          explore(row + 1, col, visited, heights[row][col])
          explore(row - 1, col, visited, heights[row][col])
          explore(row, col + 1, visited, heights[row][col])
          explore(row, col - 1, visited, heights[row][col])
            
          
        pac_set = set()
        atl_set = set()
        for row in range(len(heights)):
          for col in range(len(heights[row])):
            if row == 0 or col == 0:
              explore(row, col, pac_set, float('-inf'))
            if row == len(heights) - 1 or col == len(heights[0]) - 1:
              explore(row, col, atl_set, float('-inf'))
            
        print(list(pac_set.intersection(atl_set)))
        return list(pac_set.intersection(atl_set))
        