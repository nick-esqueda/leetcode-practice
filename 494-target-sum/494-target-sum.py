class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        mult by -1 to get the inverse
        can choose to multiply by -1 for this num or leave it
        after you get to the end of nums, sum all of those up and check against target
        if the sum == target, return 1 since you found a way to hit target
        return the sum of the different decisions
        """
        memo = {}
        def get_combos(i, run_sum):
            key = (i, run_sum)
            if key in memo:
                return memo[key]
            if i >= len(nums):
                return 1 if run_sum == target else 0 
            
            combos = 0
            combos += get_combos(i + 1, run_sum + nums[i])
            combos += get_combos(i + 1, run_sum - nums[i])
            
            memo[key] = combos
            return combos
        
        return get_combos(0, 0)