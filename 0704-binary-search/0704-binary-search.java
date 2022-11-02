class Solution {
    public int search(int[] nums, int target) {
        // return classic(nums, target);
        // return avoidOverflow(nums, target);
        return breakOnLastEle(nums, target);
    }
    
    public int breakOnLastEle(int[] nums, int target) {
        /*
        in this variation, we leave the possibility of the target being on the boundary. 
        then, whenever there is only one element left, the loop will break, and then we
        compare that final element to the target.
        depending on whether we round down to choose the lower mid or round up to choose
        the higher mid, we want to be sure that if there are only 2 ele's left, we are
        still able to move either hi or lo to close in on the last ele. otherwise, we end
        up in an infinite loop.
        i.e.
        if the target was the left of 2 ele's and you choose lower mid, then you need to
        make sure that lo doesn't just get reassigned to itself, and that hi will move in.
        if the target was the right of 2 ele's and you choose upper mid, then you need to
        make sure that hi doesn't just get reassigned to itself, and that lo will move in.
        */
        int lo = 0;
        int hi = nums.length - 1;
        
        while (lo < hi) { // break when lo and hi are pointing to the last ele.
            int mid = lo + ((hi - lo) / 2); // round down/choose left mid.
            
            if (target > nums[mid])
                lo = mid + 1;
            else 
                hi = mid;
        }
        
        return nums[lo] == target ? lo : -1;
    }
    
    public int avoidOverflow(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length - 1;
        
        while (lo <= hi) {
            // math trick to avoid integer overflow.
            // this will choose the left mid for even array lengths.
            int mid = lo + ((hi - lo) / 2);
            
            if (nums[mid] == target)
                return mid;
            else if (target < nums[mid])
                hi = mid - 1;
            else 
                lo = mid + 1;
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