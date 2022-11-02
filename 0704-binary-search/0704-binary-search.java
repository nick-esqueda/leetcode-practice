class Solution {
    public int search(int[] nums, int target) {
        // return classic(nums, target);
        return avoidOverflow(nums, target);
    }
    
    public int avoidOverflow(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length - 1;
        
        while (lo <= hi) {
            // math trick to avoid integer overflow.
            int mid = lo + ((hi - lo) / 2);
            
            if (nums[mid] == target) {
                return mid;
            } else if (target < nums[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        
        return -1;
    }
    
    public int classic(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length - 1;
        
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            
            if (nums[mid] == target) {
                return mid;
            } else if (target > nums[mid]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        
        return -1;
    }
}  