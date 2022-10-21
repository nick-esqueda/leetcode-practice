class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // return bruteForce(nums);
        // return twoPointer(nums);
        // return set(nums);
        return noSort(nums);
    }
    
    public List<List<Integer>> noSort(int[] nums) {
        /*
            can get around sorting by using a set for res.
            anytime you add another duplicate triplet, it will get 
            filtered out by the set.
            convert to ArrayList at the end.
        */
        
        Set<List<Integer>> res = new HashSet<>();
        Set<Integer> iSeen = new HashSet<>();
        
        for (int i = 0; i < nums.length - 2; ++i) {
            if (iSeen.contains(nums[i])) continue; // small optimization.
            iSeen.add(nums[i]);
            Set<Integer> compliments = new HashSet<>();
            
            for (int j = i + 1; j < nums.length; ++j) {
                int comp = -(nums[i] + nums[j]);
                if (compliments.contains(comp)) {
                    List<Integer> trip = Arrays.asList(nums[i], nums[j], comp);
                    Collections.sort(trip);
                    res.add(trip);
                }
                    
                compliments.add(nums[j]);
            }
        }
        
        return new ArrayList(res);
    }
    
    public List<List<Integer>> set(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 2; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            Set<Integer> compliments = new HashSet<>();
            
            for (int j = i + 1; j < nums.length; ++j) {
                int compli = -(nums[i] + nums[j]); 
                if (compliments.contains(compli)) {
                    res.add(Arrays.asList(nums[i], nums[j], compli));
                    
                    // REMINDER: ++j will occur again after for loop iteration.
                    while (j + 1 < nums.length && nums[j] == nums[j + 1]) {
                        j += 1;
                    }
                }
                
                compliments.add(nums[j]);
            }
        }
        
        return res;
    }
    
    public List<List<Integer>> twoPointer(int[] nums) {       
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 2; ++i) {
            // avoid duplicates of i.
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int L = i + 1;
            int R = nums.length - 1;
            
            while (L < R) {
                int sum = nums[i] + nums[L] + nums[R];
                
                if (sum < 0) {
                    L += 1;
                } else if (sum > 0) {
                    R -= 1;
                } else {
                    List<Integer> trip = Arrays.asList(nums[i], nums[L++], nums[R--]);
                    res.add(trip);
                    
                    // make sure L doesn't land on a duplicate. 
                    while (L < R && nums[L] == nums[L - 1]) {
                        L += 1;
                    }
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
        
        for (int i = 0; i < nums.length; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            for (int j = i + 1; j < nums.length; ++j) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }

                for (int k = j + 1; k < nums.length; ++k) {
                    if (k > j + 1 && nums[k] == nums[k - 1]) {
                        continue;
                    }
                    
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> trip = Arrays.asList(nums[i], nums[j], nums[k]);
                        res.add(new ArrayList<>(trip));
                    } 
                }
            }
        }
        
        return res;
    }
}