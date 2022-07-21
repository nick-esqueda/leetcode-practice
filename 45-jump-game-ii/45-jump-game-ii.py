class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def get_shortest(i):
            if i in memo:
                return memo[i]
            if i >= len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            
            min_jumps = float('inf')
            jumps = nums[i]
            for dist in range(1, jumps + 1):
                min_jumps = min(min_jumps, 1 + get_shortest(i + dist))

            memo[i] = min_jumps
            return min_jumps
        
        return get_shortest(0)
            
