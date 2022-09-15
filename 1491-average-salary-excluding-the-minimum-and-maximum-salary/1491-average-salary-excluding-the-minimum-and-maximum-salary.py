class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal, max_sal = float('inf'), float('-inf')
        sum_ = 0
        for sal in salary:
            min_sal = min(min_sal, sal)
            max_sal = max(max_sal, sal)
            sum_ += sal
        return (sum_ - min_sal - max_sal) / (len(salary) - 2)
        
        
#     def average(self, salary: List[int]) -> float:
#         """
        
#         """
#         min_sal = min(salary)
#         max_sal = max(salary)        
#         return (sum(salary) - min_sal - max_sal) / (len(salary) - 2)