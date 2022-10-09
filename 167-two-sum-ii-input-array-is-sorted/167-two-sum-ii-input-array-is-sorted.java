class Solution {
    public int[] twoSum(int[] numbers, int target) {
        return twoPointer(numbers, target);
    }
    
    public int[] twoPointer(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        
        while (l < r) {
            int sum = nums[l] + nums[r];
            if (sum < target) {
                l += 1;
            } else if (sum > target) {
                r -= 1;
            } else {
                return new int[] {l + 1, r + 1};
            }
        }
        
        return null;
    }
}