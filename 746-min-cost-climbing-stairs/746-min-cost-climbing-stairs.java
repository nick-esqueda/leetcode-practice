class Solution {
    public Map<Integer, Integer> memo = new HashMap<>();
    
    public int minCostClimbingStairs(int[] cost) {
        /*
            the min cost to reach the i'th floor is 
            
            why is it a DP problem? because we have a few things:
                    - state
                        - i
                    - base cases:
                        - if the size of the array is 2, then the min cost to reach the top is the min of idx 0 and 1
                        - if the size of the array is 1, the min cost to the top is 0...???
                        - OR??? -
                        - if you are at the top..................
                    - subproblems:
                        - we can use the min cost of the subarray with -1 size and -2 size to find the min cost to the top of the whole array
                    
            at the i'th position you know that you can only get there from 1 step or 2 steps back.
            since this is a fact, you know that taking the min of...
                - the min cost to get to the top of the subarray ending at i - 1, plus(+) the cost at i - 1
                - AND -
                - the min cost to get to the top of the subarray ending at i - 2, plus(+) the cost at i - 2
             ... will get you the min cost to reach the top of the array stopping at i.
             
             RECURRENCE RELATION:
             dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            
            
            ???:
            can you conceptually do this forwards and backwards? (starting at the beginning vs. the end of the array)
            
            why do i not have to take the min of i=0 and i=1 again...?
        */
        
        return minCostTopDown(cost, cost.length);
        // return minCostBottomUp(cost);
    }
    
    public int minCostTopDown(int[] cost, int topIndex) {
        if (topIndex == 1) return 0;
        if (topIndex == 2) return Math.min(cost[0], cost[1]);
        
        if (!memo.containsKey(topIndex)) {
            int minCost = Math.min(minCostTopDown(cost, topIndex - 1) + cost[topIndex - 1], 
                                   minCostTopDown(cost, topIndex - 2) + cost[topIndex - 2]);
            memo.put(topIndex, minCost); 
        }
        
        return memo.get(topIndex);
    }
    
    public int minCostBottomUp(int[] cost) {
        if (cost.length == 2) return Math.min(cost[0], cost[1]);
        
        int[] tab = new int[cost.length + 1];
        tab[1] = 0;
        tab[2] = Math.min(cost[0], cost[1]);
        
        for (int i = 3; i <= cost.length; ++i) {
            tab[i] = Math.min(tab[i - 1] + cost[i - 1],
                              tab[i - 2] + cost[i - 2]);
        }
        
        return tab[tab.length - 1];        
    }
}