class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length <= 1) return nums.length;
        
        // return bruteForce(nums);
        return setSequence(nums);
    }
    
    public int setSequence(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num: nums) set.add(num);
        
        int maxCount = 1;
        for (int num: set) {
            // only if this num is the start of a sequence...
            if (!set.contains(num - 1)) { 
                // go through the sequence and keep count.
                int currNum = num;
                int count = 1;
                while (set.contains(currNum + 1)) { 
                    count++; 
                    currNum++;
                }
                
                maxCount = Math.max(maxCount, count);
            }
        }
        
        return maxCount;
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