class Solution:
    def average(self, salary: List[int]) -> float:
        """
        
        """
        min_sal = min(salary)
        max_sal = max(salary)        
        return (sum(salary) - min_sal - max_sal) / (len(salary) - 2)