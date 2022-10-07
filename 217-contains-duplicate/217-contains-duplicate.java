class Solution {
    public boolean containsDuplicate(int[] nums) {
        // return brute(nums); // O(n^2) time | TLE
        // return sorting(nums); // O(nlogn) time
        return set(nums); // O(n) time
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
    
    public boolean brute(int[] nums) { // TLE
        for (int i = 0; i < nums.length; ++i) {
            for (int j = i + 1; j < nums.length; ++j) {
                if (nums[j] == nums[i]) return true;
            }
        }
        
        return false;
    }
}