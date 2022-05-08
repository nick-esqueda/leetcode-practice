class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        set lo pointer to 0 (A)
        set hi pointer to [-1] (B)
        while the pointers are not overlapping...
        calc a midpoint
        if the value is at the midpoint, return the midpoint index
        if the value is at A or B, return that index
        if the value is greater than the midpoint, move lo pointer to mid + 1 
        if the value is less than the midpoint, move hi pointer to mid - 1 
        
        if no return inside while loop, return -1
        """
        
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
          midpoint = (hi + lo) // 2
          print(midpoint)
          
          if nums[midpoint] == target:
            return midpoint
          if nums[lo] == target:
            return lo
          if nums[hi] == target:
            return hi
          
          if target > nums[midpoint]:
            lo = midpoint + 1
          
          if target < nums[midpoint]:
            hi = midpoint - 1
        
        return -1