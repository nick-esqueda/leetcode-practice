class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        have a count of open and close parens
        can choose to add an open or a close depending on some conditions:
            if open - close == 0, can add an open but not a close
            if open - close > 0, can add either open or close
            can only add n number of open or close
                (in other words, if open count > n, can't add any more opens)
        whenever open and close counts are both == n, append that string to rtn list
        """
        rtn = []
        
        def backtrack(parens, opening, closing):
            if opening == n and closing == n:
                rtn.append(''.join(parens))
                return
            
            if opening < n:
                parens.append("(")
                backtrack(parens, opening + 1, closing)
                parens.pop()
            if opening - closing > 0:
                parens.append(")")
                backtrack(parens, opening, closing + 1)
                parens.pop()
            
        backtrack([], 0, 0)
        return rtn