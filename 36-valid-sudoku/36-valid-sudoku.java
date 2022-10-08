class Solution {
    public boolean isValidSudoku(char[][] board) {
        /*
            throw each char into a set, and count how many chars.
            if the count != set.size(), there was a duplicate
            > make sure rows don't have duplicates
                new set for each row
            > make sure cols don't have duplicates
                new set for each col

            make sure boxes don't have duplicates
                9 different sets for each box.
                use map to determine the correct group:
                    > (2, 0): set(1, 6, 4)
                divide each real idx by 3 to get correct group.
        */
        
        // CHECK ROWS
        for (int row = 0; row < board.length; ++row) {
            Set<Character> rowSet = new HashSet<>();
            for (int col = 0; col < board.length; ++col) {
                char c = board[row][col];
                if (rowSet.contains(c)) return false;
                if (c != '.') rowSet.add(c);
            }
        }
        
        // CHECK COLS
        for (int col = 0; col < board.length; ++col) {
            Set<Character> colSet = new HashSet<>();
            for (int row = 0; row < board.length; ++row) {
                char c = board[row][col];
                if (colSet.contains(c)) return false;
                if (c != '.') colSet.add(c);
            }
        }
        
        // build the box set mappings.
        Map<String, Set<Character>> boxes = new HashMap<>();
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                StringBuilder group = new StringBuilder();
                group.append(i);
                group.append(",");
                group.append(j);
                
                boxes.put(group.toString(), new HashSet<>());
            }
        }
        
        // CHECK BOXES
        for (int i = 0; i < board.length; ++i) {
            for (int j = 0; j < board.length; ++j) {
                StringBuilder group = new StringBuilder();
                group.append(i / 3);
                group.append(',');
                group.append(j / 3);
                
                char c = board[i][j];
                if (boxes.get(group.toString()).contains(c)) {
                    return false;
                }
                if (c != '.') {
                    boxes.get(group.toString()).add(c);
                }
            }
        }
        
        return true;
    }
}