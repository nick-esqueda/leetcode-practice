class Solution {
    public int numIslands(char[][] grid) {
        int island_count = 0;
        for (int row = 0; row < grid.length; ++row) {
            for (int col = 0; col < grid[0].length; ++col) {
                if (grid[row][col] == '1') {
                    dfs(row, col, grid);
                    island_count += 1;
                }
            }
        }
        
        return island_count;
    }
    
    private void dfs(int r, int c, char[][] matrix) {
        if (r < 0 || r == matrix.length ||
            c < 0 || c == matrix[0].length ||
            matrix[r][c] == '0') {
            return;
        }
        
        matrix[r][c] = '0';
        dfs(r - 1, c, matrix);
        dfs(r + 1, c, matrix);
        dfs(r, c - 1, matrix);
        dfs(r, c + 1, matrix);
    }
}