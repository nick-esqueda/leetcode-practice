class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();
    
    public int climbStairs(int n) {
        /*
            the number of ways to get to the n'th step is the sum of the number of ways to get to the previous step and the 2nd previous step.
            dp(i) = dp(i - 1) + dp(i - 2)
            base cases:
                constraint - lowest n can be is 1, so if n == 1, there is only 1 way to climb to the top.
                if n is 2, then there are two ways to climb to the top.
        */
        
        return get_ways(n);
    }
    
    private int get_ways(int n) {
        if (n <= 2) return n;
        if (!memo.containsKey(n)) {
            int num_ways = get_ways(n - 1) + get_ways(n - 2);
            memo.put(n, num_ways);
        }
        
        return memo.get(n);
    }
}