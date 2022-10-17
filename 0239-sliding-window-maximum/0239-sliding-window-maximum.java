class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        /*
            want the max number in each individual window.
            
            BRUTE FORCE TLE:
            go through i-j to get the maximum of each individual window.
            
            OPTIMIZED (DEQUE):
            an element is in the window if it's index is within (i - k + 1) through (i). vice versa:
            you know an ele is "out of the window (OOW)" if that ele's index is <= i - k.
            store indexes instead of ele's on the deque, so that you know to ignore that ele or not (in window or OOW).
            each iteration/new ele, remove back of deque while(){} nums[last] < nums[i]. 
            then, put the index there in the right spot.
            take deque[0] to be the max in the window (unless it's OOW, then remove until in window.)
            only take max if the window is ready/has met k length (to take care of first few iterations)
            
            res = [3, 3, -1, 5, 5, 6, 7]
            q =   [7(8)] now, window is at size k. next iter...
            i - k = 5 --> OOB: false
            
                                        i
             0  1   2   3   4  5  6  7  8
            [1  3  -1] -3  -5  5  3  6  7       3
             1 [3  -1  -3] -5  5  3  6  7       3
             1  3 [-1  -3  -5] 5  3  6  7       -1
             1  3  -1 [-3  -5  5] 3  6  7       5
             1  3  -1  -3 [-5  5  3] 6  7       5
             1  3  -1  -3  -5 [5  3  6] 7       6
             1  3  -1  -3  -5  5 [3  6  7]      7
        */   
        
        // return bruteForce(nums, k);
        return deque(nums, k);
    }
    
    public int[] deque(int[] nums, int k) {
        int[] res = new int[nums.length - k + 1];
        Deque<Integer> deque = new ArrayDeque<>();
        
        for (int r = 0; r < nums.length; ++r) {
            int l = r - k + 1;
            
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[r]) {
                int popped = deque.pollLast(); // remove back of deque to find spot for curr num.
            }
            
            deque.offer(r);
            
            while (deque.peekFirst() < l) {
                deque.pollFirst(); // remove index at front if it's OOW.
            }
            
            // add to res (only if the window is ready)
            if (l >= 0) res[l] = nums[deque.peekFirst()];
        }
        
        return res;
    }
    
    public int[] bruteForce(int[] nums, int k) {
        int[] res = new int[nums.length - k + 1];
        
        int j = k - 1;
        for (int i = 0; j < nums.length; ++i) {
            res[i] = findMax(nums, i, j);            
            j += 1;
        }
        
        return res;
    }
    
    public int findMax(int[] nums, int start, int end) {
        int max = Integer.MIN_VALUE;
        for (int i = start; i <= end; ++i) {
            max = Math.max(max, nums[i]);
        }
        
        return max;
    }
}