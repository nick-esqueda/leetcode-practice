class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        can you rearrange the array so that the difference between each pair of consecutive numbers is the same?
        """
        arr.sort()
        
        diff = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != diff:
                return False
            
        return True
            