class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.two_pass_bs(nums, target)


    def two_pass_bs(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        first = self.bs_first_or_last(nums, target, True)
        last = self.bs_first_or_last(nums, target, False)

        return [first, last] if nums[first] == target else [-1, -1]


    def bs_first_or_last(self, nums: List[int], target: int, isFirst: bool) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if isFirst:
                mid = lo + ((hi - lo) // 2)
                if target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                mid = lo + ((hi - lo + 1) // 2)
                if target >= nums[mid]:
                    lo = mid
                else:
                    hi = mid - 1
        
        return lo
