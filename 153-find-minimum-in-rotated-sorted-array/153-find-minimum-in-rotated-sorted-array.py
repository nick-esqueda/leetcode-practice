class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [4,5,6,7,0,1,2]
                 l m r
                 
        [3,4,5,1,2]
              ml r
              
        [3,4,5,1,2]
        
        [8,10,16,22]
        [10,16,22,8]
        [16,22,8,10]
        
        """
        cur_min = float('inf')
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            cur_min = cur_min = min(cur_min, nums[mid])
            
            if nums[lo] <= nums[mid] <= nums[hi]:
                cur_min = min(cur_min, nums[lo])
                break
                
            if nums[lo] <= nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return cur_min

            
                
