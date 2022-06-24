class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        """
        if len(digits) == 0:
            return ""
        
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        all_combinations = []
        combination = []
        
        def get_combinations(i):
            if i >= len(digits):
                all_combinations.append(''.join(combination))
                return
            
            digit = digits[i]
            for letter in phone[digit]:
                combination.append(letter)
                get_combinations(i + 1)
                combination.pop()
            
        get_combinations(0)
        return all_combinations
            