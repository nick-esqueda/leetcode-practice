class Solution {
    public boolean isHappy(int n) {
        /*

        */
        
        Set<Integer> vis = new HashSet<>();
        
        while (n != 1) {
            if (vis.contains(n)) return false;
            vis.add(n);
            
            int digitSum = 0;
            while (n != 0) {
                int digit = n % 10;
                digitSum += Math.pow(digit, 2);
                n /= 10;
            }
            
            n = digitSum;
        }
        
        return true;
    }
}