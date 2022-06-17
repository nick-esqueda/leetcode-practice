class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        """
        # rows
        for r in range(len(board)):
            row_set = set()
            for c in range(len(board[r])):
                num = board[r][c]
                if num in row_set:
                    return False  
                else:
                    if num != ".":
                        row_set.add(num)
             
        # cols
        for c in range(len(board[0])):
            col_set = set()
            for r in range(len(board)):
                num = board[r][c]
                if num in col_set:
                    return False
                else:
                    if num != ".":
                        col_set.add(num)
        # 3x3
        subbox_sets = {}
        for r in range(3):
            for c in range(3):
                subbox_sets[(r, c)] = set()
                
        for r in range(len(board)):
            for c in range(len(board[r])):
                num = board[r][c]
                if num in subbox_sets[(r//3, c//3)]:
                    return False
                else:
                    if num != ".":
                        subbox_sets[(r//3, c//3)].add(num)

        return True