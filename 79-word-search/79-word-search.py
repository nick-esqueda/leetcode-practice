class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        loop through every pos in grid
        if you come across the first letter, start off a traversal
        if the trav comes back as True, return True
        else, keep iterating
        after iterating through every pos, return False
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if self.explore(board, r, c, 0, word, set()) is True:
                        return True
        return False
        

    def explore(self, board, r, c, i, s, vis):
        """
        if the coords are out of bounds, return False
        if the pos is not the cur letter, return False
        if the pos is in vis, return False
        if cur letter is last letter and the pos == last letter, early return True 
        add pos to vis
        explore() all 4 directions
        if any of those explorations return True, return True
        remove from visited so you can reuse pos's that might have been visited earlier
        return False if explored all directions without early return
        
        [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]]
        "ABCESEEEFS"
        """
        pos = (r, c)
        if r not in range(len(board)) or c not in range(len(board[0])):
            return False
        if pos in vis:
            return False
        if board[r][c] != s[i]:
            return False
        if i == len(s) - 1 and board[r][c] == s[i]:
            return True
        
        vis.add(pos)
        if (
            self.explore(board, r - 1, c, i + 1, s, vis) or
            self.explore(board, r + 1, c, i + 1, s, vis) or
            self.explore(board, r, c - 1, i + 1, s, vis) or
            self.explore(board, r, c + 1, i + 1, s, vis)
        ):
            return True

        vis.remove(pos)
        return False
        
        
