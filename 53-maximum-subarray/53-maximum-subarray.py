class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        run_sum = 0
        for num in nums:
            run_sum += num
            if num > run_sum:
                run_sum = num
            max_sum = max(max_sum, run_sum)
        return max_sum