class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        if you decide to use a num, you must move on
        if you decide NOT to use a num, you have to move on anyways
        
        DUPLICATES:
        since there are duplicate candidates, you need to make sure that you don't use that duplicate in the other subtree
        if you take a num that's a duplicate, you can keep taking that duplicate to get those combinations
        if you don't take a duplicate, you need to never take that sum num (iterate until you find new num)
        """
        candidates.sort()
        all_combos = []
        combo = []
        
        def get_combs(i, target):
            if target == 0:
                all_combos.append(combo[::])
                return
            if target < 0:
                return
            if i >= len(candidates):
                return
            
            num = candidates[i]
            combo.append(num)
            print(combo)
            get_combs(i + 1, target - num)
            
            combo.pop()
            while i < len(candidates) and candidates[i] == num:
                i += 1
            get_combs(i, target)
            return
        
        get_combs(0, target)
        return all_combos
