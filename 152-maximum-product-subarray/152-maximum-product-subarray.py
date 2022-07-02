class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        consecutive positive numers will always make the product greater
        if you have negative values, they will invert the product
        when you come across a negative, you could use the minimum (most negative) product subarray before cur num to get a pos num
        when you come across a zero, need to reset the running max and min values since the streak would have ended
            - actually, don't need to do this because you will eventually find a max value that is greater than zero, and you don't 
                have to multiply that num by 0 in order to make it become the new max
        """
        run_min, run_max = 1, 1
        rtn = float('-inf')
        for num in nums:
            temp_max = run_max * num
            run_max = max(temp_max, run_min * num, num)
            run_min = min(run_min * num, temp_max, num)
            rtn = max(run_max, rtn)
        return rtn
            
        