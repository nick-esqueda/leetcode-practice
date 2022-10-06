class Solution {
    public boolean isHappy(int n) {
        /*

        */
        
        Set<Integer> seen = new HashSet<>();
        
        while (n != 1) {
            if (seen.contains(n)) return false;
            seen.add(n);
            n = sumDigitSquares(n);
        }
        
        return true;
    }
    
    public int sumDigitSquares(int n) {
        int digitSum = 0;
        while (n != 0) {
            int digit = n % 10;
            digitSum += Math.pow(digit, 2);
            n /= 10;
        }
        
        return digitSum;
    }
}