class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
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