class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        since nums are sorted, can set two pointers on either side of array and inc/dec to get proper sum
        """
        i, j = 0, len(numbers) - 1
        while i != j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]
        
                
