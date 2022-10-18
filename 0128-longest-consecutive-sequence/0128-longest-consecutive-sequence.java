class Solution {
    public int longestConsecutive(int[] nums) {
        // if (nums.length <= 1) return nums.length;
        
        // return bruteForce(nums);
        // return sorting(nums);
        return setSequence(nums);
    }
    
    public int setSequence(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) numSet.add(num);
        int maxLen = 0;
        
        for (int num : numSet) {
            if (!numSet.contains(num - 1)) {
                int len = 0;
                while (numSet.contains(num)) {
                    len += 1;
                    num += 1;
                }
                
                maxLen = Math.max(maxLen, len);
            }
        }
        
        return maxLen;
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