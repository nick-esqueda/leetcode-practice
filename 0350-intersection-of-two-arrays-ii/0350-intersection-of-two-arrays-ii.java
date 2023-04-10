class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> nums1Counts = new HashMap<>();
        Map<Integer, Integer> nums2Counts = new HashMap<>();
        
        // get the count of each occurrence of every number in either array.
        int longestArrayLength = Math.max(nums1.length, nums2.length);
        for (int i = 0; i < longestArrayLength; ++i) {
            if (i < nums1.length) {
                int num = nums1[i];
                int previousCount  = nums1Counts.getOrDefault(num, 0);
                nums1Counts.put(num, previousCount + 1);
            }
            
            if (i < nums2.length) {
                int num = nums2[i];
                int previousCount  = nums2Counts.getOrDefault(num, 0);
                nums2Counts.put(num, previousCount + 1);
            }
        }
        
        // for the nums that are in both maps (arrays), add the least number of occurrences to the output.
        List<Integer> intersection = new ArrayList<>();
        for (int num1 : nums1Counts.keySet()) {
            if (nums2Counts.containsKey(num1)) {
                int leastOccurrences = Math.min(nums1Counts.get(num1), nums2Counts.get(num1));
                for (int i = 0; i < leastOccurrences; ++i) {
                    intersection.add(num1);
                }
            }
        }
        
        return intersection.stream().mapToInt(i -> i).toArray();
    }
}