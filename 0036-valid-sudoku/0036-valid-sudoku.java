class Solution {
    public boolean isValidSudoku(char[][] board) {
        /*
            make sure each row contains no dups.
            make sure each col conatins no dups.
            make sure each block contains no dups.
            
            to find the block that a coord belongs to: (r//3 * 3) + c//3
            find the group coords, i.e. (0, 1), and the expand out to fit within 0-8. 
             0,0 | 0,1 | 0,2 | 1,0 | 1,1 | 1,2 | 2,0 | 2,1 | 2,2
            [     row 1      |      row 2      |      row 3     ]
              0     1     2     3     4     5     6     7     8
        */
        
        // CHECK ROWS
        for (int row = 0; row < 9; ++row) {
            int[] hasNum = new int[10]; // numbers 1-9, 0th idx not used.
            for (int col = 0; col < 9; ++col) {
                char c = board[row][col];
                if (c == '.') continue;
                
                int num = Character.getNumericValue(c);
                if (hasNum[num] == 1) return false;
                hasNum[num] = 1;
            }
        }
        
        // CHECK COLS
        for (int col = 0; col < 9; ++col) {
            int[] hasNum = new int[10]; // numbers 1-9, 0th idx not used.
            for (int row = 0; row < 9; ++row) {
                char c = board[row][col];
                if (c == '.') continue;
                
                int num = Character.getNumericValue(c);
                if (hasNum[num] == 1) return false;
                hasNum[num] = 1;
            }
        }
        
        // CHECK BOXES
        int[][] blocks = new int[9][10];
        for (int row = 0; row < 9; ++row) {
            for (int col = 0; col < 9; ++col) {
                char c = board[row][col];
                if (c == '.') continue;
                
                int num = Character.getNumericValue(c);
                int blockNum = ((row / 3) * 3) + (col / 3);
                
                if (blocks[blockNum][num] == 1) return false;
                blocks[blockNum][num] = 1;
            }
        }
        
        
        return true;
    }
}