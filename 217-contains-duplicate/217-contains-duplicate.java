class Solution {
    public boolean containsDuplicate(int[] nums) {
        return set(nums);
    }
    
    public boolean set(int[] nums) {
        Set<Integer> set = new HashSet<>();
        
        for (int num : nums) {
            if (set.contains(num)) return true;
            set.add(num);
        }
        
        return false;
    }
}