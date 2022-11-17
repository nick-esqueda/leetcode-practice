class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) # must be 1 + the last index in case we need to insert at the end.

        while lo < hi:
            mid = (hi + lo) // 2 # left mid

            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                # include mid in the boundary, since it could 
                # still be an acceptable insertion point.
                hi = mid 
            else: 
                lo = mid + 1

        return lo
