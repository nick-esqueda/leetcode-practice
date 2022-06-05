class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        can get all permutations by removing one element, getting all of the perms of that subarray,
          and then adding the element back in and shifting it through the array
        if nums is empty, return [[]]
        """
        if not nums:
          return [[]]
        
        last = nums.pop()
        perms = self.permute(nums)
        
        all_perms = []
        for perm in perms:
          for i in range(len(perm) + 1):
            all_perms.append([*perm[:i], last, *perm[i:]])
            
        return all_perms
        