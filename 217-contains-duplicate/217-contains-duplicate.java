class Solution {
    public boolean containsDuplicate(int[] nums) {
        // return set(nums);
        return sorting(nums);
    }
    
    public boolean set(int[] nums) {
        Set<Integer> set = new HashSet<>();
        
        for (int num : nums) {
            if (set.contains(num)) return true;
            set.add(num);
        }
        
        return false;
    }
    
    public boolean sorting(int[] nums) {
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 1; ++i) {
            if (nums[i] == nums[i + 1]) return true;
        }
        
        return false;
    }
}