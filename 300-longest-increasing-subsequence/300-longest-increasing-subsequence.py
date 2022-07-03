class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        look for all nums that are greater than the current num
        once you find one, get the LIS from the tab and add one (self) to it
        take the max of all of those LIS's, and assign that in the tab
        """
        tab = [0] * (len(nums) + 1)
        rtn = 0
        for i in range(len(nums)-1, -1, -1):
            max_tab = 0
            j = i
            while j < len(nums):
                if nums[j] > nums[i]:
                    max_tab = max(tab[j], max_tab)
                j += 1
            tab[i] = max(1, 1 + max_tab)
            rtn = max(tab[i], rtn)
        return rtn
