class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        can move two pointers around to represent 'levels'
        each level will contain all of the vals you can use to jump
        set the hi pointer to the farthest idx you could jump to
        set lo to hi+1
        increment count because you just moved on another level
        loop through everything again until your right pointer is out of bounds
        """
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            max_jump = 0
            for i in range(l, r + 1): # loop through level to get the farthest index
                max_jump = max(max_jump, i + nums[i])
            l, r = r + 1, max_jump
            jumps += 1
        return jumps
    
    def jump_TOPDOWN(self, nums: List[int]) -> int:
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
        