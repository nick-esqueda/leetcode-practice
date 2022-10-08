class Solution {
    public int[] productExceptSelf(int[] nums) {
        // return bruteForce(nums);
        return something(nums);
    }
    
    public int[] something(int[] nums) {
        /*
            the product of all but curr num is the same as the
            product of all to the left and all to the right of curr.
            if you make two passes, you can fill up two different arrays
            that will store the "left prod" and "right prod" for every idx.
            
            L: [1*,   2, 8, 48] 
            R: [192, 48, 8, 1*]
                      i
               [2,    4, 6,  8]
        */
        
        int[] leftProds = new int[nums.length];
        int[] rightProds = new int[nums.length];
        leftProds[0] = 1;
        rightProds[rightProds.length - 1] = 1;
        
        for (int i = 1; i < nums.length; ++i)
            leftProds[i] = leftProds[i - 1] * nums[i - 1];
        
        for (int i = nums.length - 2; i >= 0; --i)
            rightProds[i] = rightProds[i + 1] * nums[i + 1];
        
        int[] answer = new int[nums.length];
        for (int i = 0; i < nums.length; ++i)
            answer[i] = leftProds[i] * rightProds[i];
    
        return answer;
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