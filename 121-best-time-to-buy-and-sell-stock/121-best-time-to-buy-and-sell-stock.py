class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        left pointer on day 1, right on day 2
        iterate day 2 throughout array
        if there was a profit from day 1 to day 2 (d2 - d1), keep left pointer, move right along
        on each iteration, if d2 - d1 > max, replace max
        if d2 < d1, move left pointer to d2, then keep iterating right pointer
        once right pointer has gone all the way through the array, return max
        """
        
        max = 0
        left = 0
        right = 1
        while right < len(prices):
          diff = prices[right] - prices[left]
          if diff > max:
            max = diff
            
          if prices[right] < prices[left]:
            left = right
          
          right += 1

        return max