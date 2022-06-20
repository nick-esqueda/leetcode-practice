class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        decide whether or not to use a number
        base cases: 
            if i is OOB
            target is 0
            target is less than 0
        """
        combinations = []
        comb = []
        
        def find_combs(i, target):
            if i >= len(candidates):
                return
            if target < 0:
                return 
            if target == 0:
                combinations.append(comb[::])
                return
            
            comb.append(candidates[i])
            find_combs(i, target - candidates[i])
            
            comb.pop()
            find_combs(i + 1, target)
        
        find_combs(0, target)
        return combinations