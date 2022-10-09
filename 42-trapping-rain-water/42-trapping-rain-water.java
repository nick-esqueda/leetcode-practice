class Solution {
    public int trap(int[] height) {
        /*
            at any given index, the amount of water that could be trapped
            at that index depends on the tallest left and right boundaries.
            the min of those boundaries is as tall as the water could go.
            but, you have to subtract however tall this index is.
                > min(maxLBound, maxRBound) - height[i] = water for i.
                
            make a few passes to collect the max L/R boundaries at every i.
        */
        
        int[] maxLBounds = new int[height.length];
        int currMax = 0;
        for (int i = 0; i < height.length; ++i) {
            maxLBounds[i] = currMax;
            currMax = Math.max(currMax, height[i]);
        }
        
        int[] maxRBounds = new int[height.length];
        currMax = 0;
        for (int i = height.length - 1; i >= 0; --i) {
            maxRBounds[i] = currMax;
            currMax = Math.max(currMax, height[i]);
        }
        
        int maxArea = 0;
        for (int i = 0; i < height.length; ++i) {
            int water = Math.min(maxLBounds[i], maxRBounds[i]) - height[i];
            if (water > 0) maxArea += water;
        }
        
        return maxArea;
    }
}