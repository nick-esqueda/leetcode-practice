class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length <= 1) return nums.length;
        
        return bruteForce(nums);
    }
    
    public int bruteForce(int[] nums) {
        Arrays.sort(nums);
        
        int maxCount = 1;
        int count = 1;
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] == nums[i - 1]) continue;
            
            if (nums[i] == nums[i - 1] + 1) {
                count++;
                maxCount = Math.max(maxCount, count);
            } else {
                count = 1;  
            } 
        }
        
        return maxCount;
    }
}