class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        since there are duplicates, if you take a duplicate, you can't take another of that duplicate in the same position
            if you do, you will have two decision subtrees that look the same, yielding duplicates
        if you take counts of nums in a map, then you know that you will only start a permutation with a certain number once
            this will yield unique permutations
        as you recurse, decrement the count in the map, telling you how many of each num you have left
        after all counts are 0, add that permutation
        """
        counts = collections.Counter(nums)
        all_perms = []

        def get_perms(perm, options):
            if options == 0:
                all_perms.append(perm[::])
                return
            
            for num in counts:
                if counts[num] <= 0:
                    continue
                    
                counts[num] -= 1
                options = options - 1 if counts[num] == 0 else options
                perm.append(num)
                get_perms(perm, options)
                
                counts[num] += 1
                options = options + 1 if counts[num] == 1 else options
                perm.pop()
        
        get_perms([], len(counts))
        return all_perms