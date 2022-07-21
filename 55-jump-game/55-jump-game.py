class Solution:
    def canJump_TOPDOWN_DP(self, nums: List[int]) -> bool:
        """
        try out all possible jumping distances and see if one of those paths gets you to the last idx
        can store the result of a spot so that you don't do repeated work
        """
        memo = {}
        def jump(i):
            if i in memo:
                return memo[i]
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
        
            jumps = nums[i]
            for j in range(1, jumps + 1):
                if jump(i + j):
                    memo[i] = True
                    return True
                
            memo[i] = False
            return False
        
        return jump(0)

    def canJump(self, nums: List[int]) -> bool:
        """
        start from the back and see if previous indices can get to the end
        you can move the 'target' index to shoot for back if you have an idx that can reach it
        if the target gets moved all the way back to 0, then you can get to the end. if not, you can't
        """
        target = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0
