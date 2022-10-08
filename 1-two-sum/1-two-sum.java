class Solution {
    public int[] twoSum(int[] nums, int target) {
        // return bruteForce(nums, target);
        return map(nums, target);
    }
    
    public int[] map(int[] nums, int target) {
        // is the compliment to curr in there? if so, return. else, just put this num and the index because it could be someone elses compliment
        Map<Integer, Integer> compliments = new HashMap<>();
        
        for (int i = 0; i < nums.length; ++i) {
            int compliment = target - nums[i];
            
            if (compliments.containsKey(compliment)) {
                return new int[] { i, compliments.get(compliment) };
            }
            
            compliments.put(nums[i], i);
        }
        
        return null;
    }
    
    public int[] bruteForce(int[] nums, int target) {
        for (int i = 0; i < nums.length; ++i) {
            for (int j = i + 1; j < nums.length; ++j) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        
        return null;
    }
}