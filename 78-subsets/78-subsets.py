class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        subset = []
        
        def get_subsets(i):
            if i > len(nums):
                return
            if i == len(nums):
                all_subsets.append(subset[::])
                return
            
            subset.append(nums[i])
            get_subsets(i + 1)
            
            subset.pop()
            get_subsets(i + 1)
        
        get_subsets(0)
        return all_subsets
