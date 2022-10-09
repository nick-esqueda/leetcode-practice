class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length <= 1) return nums.length;
        
        // return bruteForce(nums);
        // return sorting(nums);
        return setSequence(nums);
    }
    
    public int setSequence(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num: nums) set.add(num);
        
        int maxCount = 1;
        for (int num : set) {
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
    
    public int sorting(int[] nums) {
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
    
    public int bruteForce(int[] nums) {       
        List<Integer> numsList = new ArrayList<>();
        for (int num : nums) numsList.add(num);
        
        int maxCount = 1;
        for (int num : nums) {
            int count = 1;
            int currNum = num;
            while (numsList.contains(currNum + 1)) {
                count += 1;
                currNum += 1;
            }
            
            maxCount = Math.max(maxCount, count);
        }
        
        return maxCount;
    }
}