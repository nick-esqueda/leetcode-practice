class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // return bruteForce(nums1, nums2);
        return bruteForceOpt(nums1, nums2);
    }
    
    public int[] bruteForceOpt(int[] nums1, int[] nums2) {
        Map<Integer, Integer> valMap = new HashMap<>();
        for (int i = 0; i < nums2.length; ++i) {
            valMap.put(nums2[i], i);           
        }
        
        int[] res = new int[nums1.length];
        
        for (int i = 0; i < nums1.length; ++i) {
            int target = nums1[i];
            int targetIdx = valMap.get(target);
            int nge = -1;
            for (int j = targetIdx + 1; j < nums2.length; ++j) {
                if (nums2[j] > target) {
                    nge = nums2[j];
                    break;
                }
            }
            
            res[i] = nge;
        }
        
        return res;
    }
    
    public int[] bruteForce(int[] nums1, int[] nums2) {
        int[] ans = new int[nums1.length];
        
        for (int i = 0; i < nums1.length; ++i) {
            int target = nums1[i];
            boolean found = false;
            int nge = -1;
            for (int j = 0; j < nums2.length; ++j) {
                if (nums2[j] == target) found = true;
                
                if (found && nums2[j] > target) {
                    nge = nums2[j];
                    break;
                }
            }
            
            ans[i] = nge;
        }
        
        return ans;
    }
}