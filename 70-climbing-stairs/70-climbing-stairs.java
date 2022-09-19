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
        
        if (n == 1) return 1;
        
        // return getWaysTopDown(n);
        return getWaysBottomUp(n);
    }
    
    private int getWaysTopDown(int n) {
        if (n <= 2) return n;
        if (!memo.containsKey(n)) {
            int num_ways = getWaysTopDown(n - 1) + getWaysTopDown(n - 2);
            memo.put(n, num_ways);
        }
        
        return memo.get(n);
    }
    
    private int getWaysBottomUp(int n) {
        int[] tab = new int[n + 1];
        tab[1] = 1;
        tab[2] = 2;
                
        for (int i = 3; i <= n; ++i)
            tab[i] = tab[i - 1] + tab[i - 2];
        
        return tab[tab.length - 1];
    }
}