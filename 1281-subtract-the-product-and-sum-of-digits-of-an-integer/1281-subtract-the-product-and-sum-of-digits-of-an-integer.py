class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        divide by 10 and floor to take 1 digit at a time
        """
        sum_ = 0
        product = 1 
        while n != 0:
            last = n % 10
            sum_ += last
            product *= last
            n = n // 10
        return product - sum_
            