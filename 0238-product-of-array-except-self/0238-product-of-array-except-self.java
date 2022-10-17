class Solution {
    public int[] productExceptSelf(int[] nums) {
        // return bruteForce(nums);
        return prefixArray(nums);
    }
    
    public int[] prefixArray(int[] nums) {
        /*
            store the prefix and suffix products of each idx.
            prefix[i] should be the product of all nums before (non-inclusive) i.
            suffix[i] should be product of all nums after (non-inclusive) i.
            multiply the prefix at suffix at each idx to get the answer.
            
                [1, 2, 3, 4]
            p = [1, 1]
            s = [24,12,4, 1]
        */
        
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        prefix[0] = 1;
        suffix[nums.length - 1] = 1;
        
        for (int i = 1; i < nums.length; ++i) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }
        for (int i = nums.length - 2; i >= 0; --i) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }
        
        int[] res = new int[nums.length];
        for (int i = 0; i < res.length; ++i) {
            res[i] = prefix[i] * suffix[i];
        }
        
        return res;        
    }
    
    public int[] bruteForce(int[] nums) {
        int[] answer = new int[nums.length];
        
        for (int i = 0; i < nums.length; ++i) {
            int product = 1;
            for (int j = 0; j < nums.length; ++j) {
                if (j == i) continue;
                
                product *= nums[j];
            }
            
            answer[i] = product;
        }
        
        return answer;
    }
}