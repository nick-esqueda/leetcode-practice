class Solution {
    public int maxArea(int[] height) {
        // return bruteForce(height);
        return optimized(height);
    }
    
    public int optimized(int[] height) {
        /*
            
            keep the larger pointer, move the smaller.
            
            [1, 8, 6, 2, 5, 4, 8, 3, 7]
                L                    R
                
            [101, 1012, 7, 99, 100]
             L                  R
        */
        
        int L = 0, R = height.length - 1;
        int maxArea = 0;
        while (L < R) {
            int area = (R - L) * Math.min(height[L], height[R]);
            maxArea = Math.max(maxArea, area);
            
            if (height[L] < height[R]) {
                L += 1;
            } else {
                R -= 1;
            }
        }
        
        return maxArea;
    }
    
    public int bruteForce(int[] height) { // TLE
        int maxArea = 0;
        for (int L = 0; L < height.length - 1; ++L) {
            for (int R = L + 1; R < height.length; ++R) {
                int area = (R - L) * Math.min(height[L], height[R]);
                maxArea = Math.max(maxArea, area);
            }
        }
        
        return maxArea;
    }
}