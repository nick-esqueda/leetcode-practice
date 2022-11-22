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
            int speed = lo + ((hi - lo) / 2); // left mid.
            int totalHours = hoursToEat(piles, speed);

            if (h >= totalHours) {
                hi = speed;
            } else {
                lo = speed + 1;
            }
        }
        
        return lo;
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