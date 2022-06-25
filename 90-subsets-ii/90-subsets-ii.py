class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        decide to use element or not
        if you've already used a duplicate element, when you decide not to use that element, make the same decision for the rest of the ele's
        in other words, if you decide not to take a duplicate, make sure all children don't take one either
        this allows for only the subtree that took the duplicate to contain all subsets with the duplicates
        """
        nums.sort()
        all_subsets = []
        subset = []
        
        def backtrack(i):
            if i >= len(nums):
                all_subsets.append(subset[::])
                return
            
            num = nums[i]
            subset.append(num)
            backtrack(i + 1)
            
            subset.pop()
            while i < len(nums) and nums[i] == num:
                i += 1
                
            backtrack(i)
            return
        
        backtrack(0)
        return all_subsets