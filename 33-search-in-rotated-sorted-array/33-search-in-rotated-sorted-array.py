class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """       
        if mid is greater than right, and the target is less, move left up (search right half)
        if mid is less than right, and the target is
        if mid is between left and right, everything is normal, so move accordingly
        
        
        [3, 1] t = 1
        lm  r
        
        """
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # everything is normal
            if nums[l] <= nums[mid] <= nums[r]:
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
            
            # the split is to the left
            elif nums[l] > nums[mid]:
                if target < nums[mid] or target >= nums[l]:
                    r = mid - 1
                elif target > nums[mid]: # this could be just else?
                    l = mid + 1
                    
            # the split is to the right
            elif nums[r] < nums[mid]:
                if target > nums[mid] or target <= nums[r]:
                    l = mid + 1
                elif target < nums[mid]: # this could be just else?
                    r = mid - 1
                
        return -1
            
        
