class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subboxes = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if (num in rows[r] or
                    num in cols[c] or
                    num in subboxes[(r//3, c//3)]):
                    return False  
                else:
                    if num != ".":
                        rows[r].add(num)
                        cols[c].add(num)
                        subboxes[(r//3, c//3)].add(num)
             
        return True