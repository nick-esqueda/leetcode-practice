class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        start from the bottom right to calculate all unique paths from each spot
        the bottom row and the rightmost column will always have 1 as their path count
            - b/c you can only go one direction, up or down, without ending up out of bounds
        instead of creating a whole matrix to store the tab, you can just use one row
        need to declare a 'base case' row that will consist of all 1's which will be the bottommost row
        the last in each row that you make should be a 1 (for that last column where you can only choose down)
        iterate backwards to make a new row (use a var to make a new row)
        at each pos, add the value at r + 1 (which will be the 'base case' row) to the value at i + 1
        after that row is complete, reassign the 'base case' row to that row you just made
        iterate and create the new row again
        only do this 'm - 1' times
        return the first value in the row
        """
        last_row = [1] * n
        
        for row in range(m - 1):
            new_row = [1] * n
            for c in range(n - 2, -1, -1):
                new_row[c] = new_row[c + 1] + last_row[c]
            last_row = new_row
        return last_row[0]
    
    
    def uniquePaths_TOPDOWN(self, m: int, n: int) -> int:
        """
        add up the number of paths going to the right and down, and return that number up
        """
        def get_paths(r, c, memo):
            pos = (r, c)
            if pos in memo:
                return memo[pos]
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            
            paths = get_paths(r + 1, c, memo) + get_paths(r, c + 1, memo)
            memo[pos] = paths
            return paths
        
        return get_paths(0, 0, {})