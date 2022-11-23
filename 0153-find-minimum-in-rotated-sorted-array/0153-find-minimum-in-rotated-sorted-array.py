class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + ((hi - lo) // 2) # left mid.
            
            if nums[lo] > nums[mid]: # left has real start.
                hi = mid
            elif nums[hi] < nums[mid]: # right has real start.
                lo = mid + 1
            else: # lo -> hi is sorted, or lo == mid (bc we chose left mid)
                if nums[lo] < nums[hi]:
                    return nums[lo]
                return nums[hi]
        
        return nums[lo]
        
        """
        can't search normally, have to bin search for minimum.
        how to know though that there's a smaller number?
        i guess you can just use the ptrs to gauge, since those will span the whole search space
        actually, you kind of just want to find the breakpoint.
        that's what we're doing actually straight up, is finding the breakpoint.
        
        THOUGHTS:
        if stuff is messed up to one side, then you should go to that side.
        ? since it's off to [this side], then i should include that in the boundary?
            - NO!! you know that if hi is less than mid, then you definitely want to exclude mid bc the real start would be somewhere in there.
            - conversely, if lo is greater than mid, you don't know if the real start is here, or in there.
            
        include the mid on the right/hi boundary, because it might be the real start.
        
        the arr is unique elements.
        you can check if lo/hi is strictly </> mid?
        
        you're "looking for the fucked up shit"
        
        [3, 4, 5, 1, 2]
               m
         l
                     r
        
        
        [2, 3, 4, 5, 1]
                     m
                     l
                     r
        
        [4, 5, 6, 0, 1, 2, 3]
                  m
                  l
                  r
        
        
        [1, 2, 3, 4, 5]
        
        
        [1, 2]
         m
         l  
            r
        
        [2, 1]
        
        [1]
        """
        
        