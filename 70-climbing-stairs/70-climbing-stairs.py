class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        """
        if n < 0, return 0
        if n == 0, return 1
        can make a decision to take 1 or 2 steps
        depending on step size, decrement n on the next call
        add the return of the recursive calls to a running total
        """
        if n in memo:
          return memo[n]
        if n < 0:
          return 0
        if n == 0:
          return 1
        
        ways = 0
        ways += self.climbStairs(n - 1)
        ways += self.climbStairs(n - 2)
        memo[n] = ways
        return ways