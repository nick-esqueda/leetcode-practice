class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        can choose which element to remove to get the perms of the smaller list
        add the removed element back into all of the returned perms
        """
        if len(nums) == 1:
            return [nums]
        
        all_perms = []
        
        for i in range(len(nums)):
            copy = nums[::]
            num = copy.pop(i)
            perms = self.permute(copy)
            for perm in perms:
                perm.append(num)
                all_perms.append(perm)
                
        return all_perms
