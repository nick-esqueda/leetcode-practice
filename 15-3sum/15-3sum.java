class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // return bruteForce(nums);
        return twoPointer(nums);
    }
    
    public List<List<Integer>> twoPointer(int[] nums) {
        /*
            sort input.
            use two pointer technique with L and R to find compliments for i.
            
            [-2,0,0,2,2]
              i   L R
        */
        
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 2; ++i) {
            if (i >= 1 && nums[i] == nums[i - 1]) continue;
            int L = i + 1;
            int R = nums.length - 1;
            
            while (L < R) {
                int sum = nums[i] + nums[L] + nums[R];
                if (sum < 0) {
                    L += 1;
                } else if (sum > 0) {
                    R -= 1;
                } else {
                    res.add(Arrays.asList(nums[i], nums[L], nums[R]));
                    L += 1;
                    R -= 1;
                    
                    while (L < R && nums[L] == nums[L - 1])
                        L += 1;
                }
            }
        }
        
        return res;
    }
    
    public List<List<Integer>> bruteForce(int[] nums) { // TLE
        /*
            want three numbers to sum up to 0.
            just triple nested to see each unique triplet.
            sort array so that you can easily check if:
            if you've used this i | j | k, continue on.
            
            [-1, -1, 0, 1, 1, 2, 2, 3]
                  i  j  k
             
            [-1, -1, 2]
            [-1, 0, 1]
        */
        
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        
        int usedI = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == usedI) continue;
            int usedJ = Integer.MAX_VALUE;
            
            for (int j = i + 1; j < nums.length; ++j) {
                if (nums[j] == usedJ) continue;
                int usedK = Integer.MAX_VALUE;

                for (int k = j + 1; k < nums.length; ++k) {
                    if (nums[k] == usedK) continue;
                    
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> trip = Arrays.asList(nums[i], nums[j], nums[k]);
                        res.add(new ArrayList<>(trip));
                        
                        usedI = nums[i];
                        usedJ = nums[j];
                        usedK = nums[k];
                    } 
                }
            }
        }
        
        return res;
    }
}