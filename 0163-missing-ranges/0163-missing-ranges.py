class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        """
        def make_range(lo, hi):
            if lo == hi:
                return str(lo)
            return str(lo) + "->" + str(hi)
        
        output = []
        prev_num = lower - 1
        for i in range(len(nums) + 1):
            # NOTE: if i is at the end, set curr to be upper.
            curr_num = nums[i] if i < len(nums) else upper + 1

            # if a range exists between prev/curr, create str and append.
            if prev_num + 1 <= curr_num - 1:
                rng = make_range(prev_num + 1, curr_num - 1)
                output.append(rng)
            
            prev_num = curr_num
            
        return output
        
        
        
