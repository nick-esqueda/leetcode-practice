class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        /*
            artith prog - difference between two adjacent elements are the same.
                ex. 2, 4, 6 -> all have diff of 2
            return true if arr can be rearranged to be an arith prog.
            sort the arr so that the possible arith prog can be checked.
        */
        
        Arrays.sort(arr);
        
        int diff = arr[1] - arr[0];
        for (int i = 0; i < arr.length - 1; ++i) {
            if (arr[i + 1] - arr[i] != diff) return false;
        }
        
        return true;
    }
}