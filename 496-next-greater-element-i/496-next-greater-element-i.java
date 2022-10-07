class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        /*
            
        */
        
        int[] ans = new int[nums1.length];
        
        for (int i = 0; i < nums1.length; ++i) {
            int target = nums1[i];
            int match = -1;
            int nge = -1;
            for (int j = 0; j < nums2.length; ++j) {
                if (nums2[j] == target) match = j; // catch the start of the subprocess to find the NGE
                
                if (match == -1) continue;
                
                if (nums2[j] > nums2[match]) {
                    nge = nums2[j];
                    break;
                }
            }
            
            ans[i] = nge;
        }
        
        
        return ans;
    }
}