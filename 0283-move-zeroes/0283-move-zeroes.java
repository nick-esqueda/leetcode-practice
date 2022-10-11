class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length == 1) return;
        
        int i = 0;
        for (int j = 1; j < nums.length; ++j) {
            if (nums[i] != 0) i += 1;
            if (nums[j] != 0) swap(i, j, nums);
        }
    }
    
    public void swap(int i, int j, int[] nums) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}