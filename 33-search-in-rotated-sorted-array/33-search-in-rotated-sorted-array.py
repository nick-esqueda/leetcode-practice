class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        if the midpoint is greater than the left, the left side is still normal
        if the midpoint is less than the left, the left side has larger numbers there and starts over at some point
        if the midpoint is greater than the right, all of the numbers to the right are less than target
        if the midpoint is less than the right, the right side is still normal
        if midpoint is between two number's values, everything is like normal
        
        
        if the target is between mid and right, move lo up (mid has to be lower than right)
        if the target is between mid and left, move hi down (mid has to be higher than right)
        
        if mid is higher than right and the target is less than right, move lo up, else move hi down
        if mid is lower than left and target is higher than left, move hi down, else move lo up
        
        if the nums weren't unique, you'd run into a case where right/left == mid, and then you couldn't determine direction
        
        8
        [4,5,6,7,8,1,2,3]
         L     M       H  
        """
        
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            elif nums[mid] < target <= nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[lo] and target >= nums[lo]:
                hi = mid - 1
            elif nums[mid] > nums[hi] and target <= nums[hi]:
                lo = mid + 1
            else:
                lo += 1
                
        return -1