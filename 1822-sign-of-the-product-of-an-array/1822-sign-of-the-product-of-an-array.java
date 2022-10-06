class Solution {
    public int arraySign(int[] nums) {
        /*
            if there was ever a 0, you could return 0 immediately. 
            otherwise, return the respective number.
            NOTE: int and even long are at risk of overflowing, so can't multiply manually.
        */
        
        int sign = 1;
        for (int num: nums) {
            if (num == 0) return 0;
            if (num < 0) sign *= -1;
        }
        return sign;
    }
}