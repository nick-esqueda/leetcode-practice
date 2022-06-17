class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1, 2, 3, 4]
               i
               
        prefixes:
        [1, 1, 2, 6]
        suffixes:
        [24, 12, 4, 1]
        
        create a prefixes array that holds the product of all indices before the curr index
        do the same for suffixes/after the curr index
        now, accessing the prefix/suffix array at i will give you the product of all prev/future ele's
        loop through nums
        multiply the prefix and suffix for that index together 
        push that product to a return array
        return array after iterating through nums
        """
        
        prefixes = [1]
        i = 1
        while i < len(nums):
            product = prefixes[i - 1] * nums[i - 1]
            prefixes.append(product)
            i += 1
        print('pres', prefixes)
        
        suffixes = [0] * len(nums)
        suffixes[-1] = 1
        i = len(nums) - 2
        while i >= 0:
            suffixes[i] = suffixes[i + 1] * nums[i + 1]
            i -= 1
        print('sufs', suffixes)   
            
        rtn = []
        for i in range(len(nums)):
            rtn.append(prefixes[i] * suffixes[i])
            
        return rtn
        
        