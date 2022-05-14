class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        declare queue
        declare total_fresh count = 0
        loop through each pos
          if you come across a 2, push those coords to a queue
          if the curr pos is a 1, increment total_fresh count
        declare minute counter = 0
        while there's something on the queue...
          take the length of the queue
          for len(q) amount of times...
            pop the front of the cue (curr)
            if current is a 1, decrement total_fresh
            push all up down left right neighbors to the queue if they are a 1
          increment minute count
        return minute count if total_fresh == 0, else -1
        """
        q = []
        total_fresh = 0
        for r in range(len(grid)):
          for c in range(len(grid[r])):
            if grid[r][c] == 2:
              q.append((r, c))
            elif grid[r][c] == 1:
              total_fresh += 1
        
        minutes = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] 
        while q and total_fresh > 0:
          for i in range(len(q)):
            r, c = q.pop(0)
            for r_delta, c_delta in directions:
              nei_row, nei_col = r + r_delta, c + c_delta
              if nei_row not in range(len(grid)) or nei_col not in range(len(grid[0])):
                continue
              if grid[nei_row][nei_col] != 1:
                continue
              q.append((nei_row, nei_col))
              grid[nei_row][nei_col] = 2
              total_fresh -= 1
          minutes += 1
        
        return minutes if total_fresh == 0 else -1
