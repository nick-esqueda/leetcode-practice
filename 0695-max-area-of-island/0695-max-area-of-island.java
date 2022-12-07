class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        
        for (int r = 0; r < grid.length; ++r) {
            for (int c = 0; c < grid[0].length; ++c) {
                if (grid[r][c] == 1) {
                    int area = dfs(r, c, grid);
                    maxArea = Math.max(maxArea, area);
                }
            }
        }
        
        return maxArea;
    }
    
    private int dfs(int r, int c, int[][] matrix) {
        if (r < 0 || r == matrix.length ||
            c < 0 || c == matrix[0].length ||
            matrix[r][c] == 0) {
            return 0;
        }
        
        matrix[r][c] = 0;
        int count = 1;
        count += dfs(r - 1, c, matrix);
        count += dfs(r + 1, c, matrix);
        count += dfs(r, c - 1, matrix);
        count += dfs(r, c + 1, matrix);
        return count;
    }
}