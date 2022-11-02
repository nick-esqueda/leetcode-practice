class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // return findRow(matrix, target);
        return oneArray(matrix, target);
    }
    
    public boolean oneArray(int[][] matrix, int target) {
        /*
            0 [[ 1, 3, 5, 7]
            1 ,[10,11,16,20]
            2 ,[23,30,34,60]]
                0  1  2  3
            
            lo = 0 
            hi = 11   // <- (3 * 4) - 1 == (R * C) - 1
            mid = 5
            matrix[what row?][what col?]
            
            row
                midIdx / length of the array
                5 // 4 -> row 1
                4 // 4 -> row 1
                3 // 4 -> row 0
            col
                the remainder of the division that got you the row number
                5 / 4 -> row 1, col 1
                4 / 4 -> row 1, col 0
                3 / 4 -> row 0, col 3
        */
        
        int nRows = matrix.length;
        int nCols = matrix[0].length;
        
        int lo = 0;
        int hi = (nRows * nCols) - 1;
        
        while (lo <= hi) {
            int mid = lo + ((hi - lo) / 2);
            int midNum = matrix[mid / nCols][mid % nCols];
            
            if (target == midNum) {
                return true;
            } else if (target < midNum) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        
        return false;
    }
    
    public boolean findRow(int[][] matrix, int target) {
        for (int row = 0; row < matrix.length; ++row) {
            int firstNum = matrix[row][0];
            int lastNum = matrix[row][matrix[row].length - 1];
            
            if (firstNum <= target && target <= lastNum) {
                return binarySearch(matrix[row], target);
            }
        }
        
        return false;
    }
    
    public boolean binarySearch(int[] arr, int target) {
        int lo = 0;
        int hi = arr.length - 1;

        while (lo < hi) {
            int mid = lo + ((hi - lo) / 2);

            if (target > arr[mid]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        return arr[lo] == target;
    }
}