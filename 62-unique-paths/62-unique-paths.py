class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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