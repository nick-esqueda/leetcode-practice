class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        declare hashtable
          (this will store K:V as value:idx)
        iterate through nums
          if target - curr num is in hashset, return [hashtable[val], curr i]
          else, store the num in the hashtable with the idx as the value
        """
        comps = {}
        for i, num in enumerate(nums):
          if target - num in comps:
            return [comps[target - num], i]
          else:
            comps[num] = i