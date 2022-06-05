class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      """
      a subset can be made by getting all of the subsets of the array minus 1 element and adding that element back in
      """
      if not nums:
        return [[]]
      
      last = nums.pop()
      subs_without_last = self.subsets(nums)
      
      all_subsets = subs_without_last.copy()
      for sub in subs_without_last:
        all_subsets.append([*sub, last])
        
      return all_subsets
