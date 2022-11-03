class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        /*
        
        [ 3, 6, 7, 11] h = 8
        k -> [1, 2, ..., 11]
        
        the max eating speed you could have is max(piles) per hour. 
        this is because if you went any higher, it wouldn't matter. 
        you still have to stay at each pile until the hour is finished.
        
        to choose the eating speed (k), you just have to try k values
        until you find one that takes the same amount of hours as h.
        
        as k increases, the total hours to finish decreases.
        */
        
        // return bruteForce(piles, h);
        return binSearch(piles, h);
    }
    
    public int binSearch(int[] piles, int h) {
        List<Integer> nums = new ArrayList<>();
        for (int n : piles) nums.add(n);
        int max = Collections.max(nums);

        int lo = 1; 
        int hi = max;
        
        while (lo < hi) {
            int k = lo + ((hi - lo) / 2);
            int totalHours = hoursToEat(piles, k);
            
            // if (totalHours == h) { // finished right on time.
            //     return k;
            // } else if (h < totalHours) { // took too long.
            //     lo = k + 1;
            // } else { // finished too fast.
            //     hi = k - 1;
            // }
            
            if (h < totalHours) { // took too long.
                lo = k + 1;
            } else { // finished right on time, or a little fast.
                hi = k;
            }
        }
        
        return hi;
    }
    
    public int bruteForce(int[] piles, int h) {
        List<Integer> nums = new ArrayList<>();
        for (int n : piles) nums.add(n);
        int max = Collections.max(nums);
        
        for (int k = 1; k <= max; ++k) {
            if (hoursToEat(piles, k) == h) return k;
        }
        
        return 0;
    }
    
    public int hoursToEat(int[] piles, double k) {
        int totalHours = 0;
        for (double count : piles) {
            totalHours += (int) Math.ceil(count / k);
        }
        
        return totalHours;
    }
}