class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            
            if nums[mid] == target:
                return mid
            
            elif target < nums[mid]: # want to go left, but...
                # check if you should go right instead.
                if nums[hi] < nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif target > nums[mid]: # want to go right, but...
                # check if you should go left instead.
                if nums[lo] > nums[mid] and target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        
        return -1
        
        
        """
        PROBLEM:
        nums was rotated, possibly.
        want to find the target value in this rotated array, without rotating it.
        (nums only has unique values)


        THOUGHTS:
        if you want to go right:
            if the breakpoint is in the right:
                - just go normally anyways, because the bigger vals are there anyways
            if the breakpoint is in the left:
                - if target is >= than L, then you should go left, not right.
                - if target is < than L though, then go right like normal.
        if you want to go left:
            if the breakpoint is in the left:
                - just go normally anyways, because the smaller vals than mid are in the left regardless
            if the breakpoint is in the right:
                - if target is <= R, then you should go right, not left, because the smaller vals will be there.
                - if target is > R, then go left like normal.
        SIMPLIFIED:
        if the target is greater than mid:
            if the breakpoint is to the left and target is >= L:
                go left, not right.
            otherwise, go right like normal. (this covers two cases -... )
        if the target is less than mid:
            if the breakpoint is to the right and target is <= R:
                go right, not left.
            otherwise, go left like normal. (this covers two cases -... )
                

        ???:
        how to know that you should go in the opposite direction that you "wanted" to go in originally?
            - use if statement to check if you should go in opposite direction or not.
        
        
        EXAMPLE:
                t = 9
        [3, 5, 7, 8, 9, 1, 2]
                     m
                     l       
                     r
    
        t = 2
        [3, 5, 7, 8, 9, 1, 2]
                        m
                     l       
                            r
        
        
        [8, 9, 1, 2, 3, 5, 7]
                  m        
         l       
                           r
        
        """