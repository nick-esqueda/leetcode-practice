class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            prod *= num
            
        if prod == 0:
            return 0
        return 1 if prod > 0 else -1