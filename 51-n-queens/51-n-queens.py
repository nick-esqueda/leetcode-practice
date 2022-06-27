class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        if the coord is OOB, return
        if the coord is in the same row as a queen you already placed, return
        if the coord is in the same col as a queen you already placed, return
        if the coord is in the diag of a queen you already placed, return
        *need to figure out how to determine diagonals
        if you didn't base case out, add the new coord to the placements list
        if len(placements) == n:
            construct a chess board with the given placements and add that to a res list
            return
        put this row in a row set and the col in a col set, and all of the diag spots in a diag set
        recurse again, moving like a knight in each direction
        remove the used row from row set, col from col set, and diag from diag set
        pop from the placements list to clean up
        
        FINDING DIAGONALS:
        (-1, -1), (1, 1) // (1, -1), (-1, 1) ---> the deltas for both diagonals in either direction
        starting at a coord, add the deltas to row/col until one of them is OOB
        add each of those coords as you go along to a list
        do the same for each new coord
        """
        solutions = []
        placements = []
        cols, pos_diags, neg_diags = set(), set(), set()
        def place_queens(r):
            if r == n:
                solutions.append(make_board(placements))
                return
                
            for c in range(n):
                pos_diag, neg_diag = r + c, r - c
                if c in cols or pos_diag in pos_diags or neg_diag in neg_diags:
                    continue
                placements.append((r, c))
                cols.add(c)
                pos_diags.add(pos_diag)
                neg_diags.add(neg_diag)
                
                place_queens(r + 1)
                
                placements.pop()
                cols.remove(c)
                pos_diags.remove(pos_diag)
                neg_diags.remove(neg_diag)
                
        def make_board(placements):
            board = [["."] * n for _ in range(n)]
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if (r, c) in placements:
                        board[r][c] = 'Q'
                board[r] = ''.join(board[r])
            return board

        place_queens(0)
        return solutions
