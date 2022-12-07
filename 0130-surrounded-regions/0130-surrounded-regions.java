class Solution {
    public void solve(char[][] board) {
        int nR = board.length, nC = board[0].length;
        
        // collect all coords on the borders to mark the
        // regions that they are connected to later.
        List<int[]> borderStarts = new ArrayList<>();
        for (int c = 0; c < nC; ++c) { // top and bottom borders.
            if (board[0][c] == 'O') {
                borderStarts.add(new int[] { 0, c });
            } 
            if (board[nR - 1][c] == 'O') { // left and right borders.
                borderStarts.add(new int[] { nR - 1, c });
            }
        }
        for (int r = 0; r < nR; ++r) {
            if (board[r][0] == 'O') {
                borderStarts.add(new int[] { r, 0 });
            }
            if (board[r][nC - 1] == 'O') {
                borderStarts.add(new int[] { r, nC - 1 });
            }
        }
        
        // mark all non-surrounded regions.
        for (int[] start : borderStarts) {
            int r = start[0], c = start[1];
            markNonSurroundedRegions(r, c, board);
        }
        
        // capture remaining O's and flip back the marked regions.
        for (int r = 0; r < board.length; ++r) {
            for (int c = 0; c < board[0].length; ++c) {
                if (board[r][c] == 'O') {
                    board[r][c] = 'X';
                } else if (board[r][c] == '*') {
                    board[r][c] = 'O';
                }
            }
        }
    }
    
    private void markNonSurroundedRegions(int r, int c, char[][] board) {
        if (r < 0 || r == board.length ||
            c < 0 || c == board[0].length ||
            board[r][c] != 'O') {
            return;
        }
        
        board[r][c] = '*';
        markNonSurroundedRegions(r - 1, c, board);
        markNonSurroundedRegions(r + 1, c, board);
        markNonSurroundedRegions(r, c - 1, board);
        markNonSurroundedRegions(r, c + 1, board);
    }
}