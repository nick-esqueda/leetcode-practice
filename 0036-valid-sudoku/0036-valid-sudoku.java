class Solution {
    public boolean isValidSudoku(char[][] board) {
        /*
            make sure each row contains no dups.
            make sure each col conatins no dups.
            make sure each box contains no dups.
            
            to find the box that a coord belongs to: (r//3 * 3) + c//3
            find the group coords, i.e. (0, 1), and the expand out to fit within 0-8. 
             0,0 | 0,1 | 0,2 | 1,0 | 1,1 | 1,2 | 2,0 | 2,1 | 2,2
            [     row 1      |      row 2      |      row 3     ]
              0     1     2     3     4     5     6     7     8
        */
        
        // return arrayFlags(board);
        return arrayFlagsOnePass(board);
    }
    
    public boolean arrayFlagsOnePass(char[][] board) {
        int[][] rows = new int[9][10];
        int[][] cols = new int[9][10];
        int[][] boxes = new int[9][10];
        
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                char charNum = board[r][c];
                if (charNum == '.') continue;
                
                int num = Character.getNumericValue(charNum);
                int box = ((r / 3) * 3) + (c / 3);
                
                if (rows[r][num] == 1 ||
                    cols[c][num] == 1 ||
                    boxes[box][num] == 1) {
                    return false;
                }
                
                rows[r][num] = 1;
                cols[c][num] = 1;
                boxes[box][num] = 1;
            }
        }
        
        return true;
    }
    
    public boolean arrayFlags(char[][] board) {
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
        int[][] boxes = new int[9][10];
        for (int row = 0; row < 9; ++row) {
            for (int col = 0; col < 9; ++col) {
                char c = board[row][col];
                if (c == '.') continue;
                
                int num = Character.getNumericValue(c);
                int boxNum = ((row / 3) * 3) + (col / 3);
                
                if (boxes[boxNum][num] == 1) return false;
                boxes[boxNum][num] = 1;
            }
        }
        
        
        return true;
    }
}