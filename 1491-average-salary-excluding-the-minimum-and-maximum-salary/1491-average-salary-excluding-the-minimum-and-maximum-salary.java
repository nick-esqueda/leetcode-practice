class Solution {
    public double average(int[] salary) {
        int minSal = Integer.MAX_VALUE;
        int maxSal = Integer.MIN_VALUE;
        int sum = 0;
        
        for (int sal: salary) {
            minSal = Math.min(minSal, sal);
            maxSal = Math.max(maxSal, sal);
            sum += sal;
        }
        
        return (double) (sum - minSal - maxSal) / (salary.length - 2);
    }
}