class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        /*
        THOUGHTS:
        the greatest ele's to the back, so....
        what if you looped backwards, and put the biggest nums at the back of nums1!
        move a ptr that holds the insertion point backwards each iteration.
        what to do when one of the ptrs (a/b) move OOB?
            > just leave the array as is and return, because the rest will be sorted.
        
        
        EXAMPLES:
                        
        [1, 2, 3, 5, 6, 7]
         a  ^
        [2, 5, 6]
        b
         
        is there a case where the ^ ptr will overlap with 'a', meaning that val would get overwritten?
        
        [1, 2, 3, 4, 5, 6]
               a  ^
        [4, 5, 6]
        b
        
        [4, 5, 0, 0, 4, 5]
        a         ^
        [1, 2, 3, 4]
                  b
        */
        
        threePointersV1(nums1, m, nums2, n);
    }
    
    private void threePointersV2(int[] nums1, int m, int[] nums2, int n) {
        int insertionPoint = nums1.length - 1;
        int idx1 = m - 1;
        int idx2 = n - 1;
        
        while (idx1 >= 0 || idx2 >= 0) {     
            if (idx2 < 0) {
                return;
            }
            
            // idx2 is always in-bounds here, so idx1 could be anything.
            if (idx1 >= 0 && nums1[idx1] >= nums2[idx2]) {
                nums1[insertionPoint--] = nums1[idx1--];
            } else {
                nums1[insertionPoint--] = nums2[idx2--];
            }
        }
    }
    
    private void threePointersV1(int[] nums1, int m, int[] nums2, int n) {
        int insertionPoint = nums1.length - 1;
        int idx1 = m - 1;
        int idx2 = n - 1;
        
        while (idx1 >= 0 || idx2 >= 0) {
            if (idx1 < 0) {
                nums1[insertionPoint--] = nums2[idx2--];
            } else if (idx2 < 0) {
                nums1[insertionPoint--] = nums1[idx1--];
            } else if (nums1[idx1] >= nums2[idx2]) {
                nums1[insertionPoint--] = nums1[idx1--];
            } else {
                nums1[insertionPoint--] = nums2[idx2--];
            }
        }
    }
}