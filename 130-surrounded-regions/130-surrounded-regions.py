class Solution:
    def solve(self, board: List[List[str]]) -> None:
      """
      iterate through only the border, and when you come across an "O"...
        traverse through that connected region of "O"s and mark all of those in a "don't flip" set
      once you've ran through the whole border and marked all of the unsurrounded regions,
      iterate through every position in the board
        if the curr position is an O and NOT in the "don't flip" set, flip it
      """
      def mark(row, col, dont_flip):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
          return 
        if board[row][col] == "X":
          return
        if (row, col) in dont_flip:
          return
        
        dont_flip.add((row, col))
        mark(row - 1, col, dont_flip)
        mark(row + 1, col, dont_flip)
        mark(row, col - 1, dont_flip)
        mark(row, col + 1, dont_flip)
        return
      
      dont_flip = set()
      for row in range(len(board)):
        for col in range(len(board[0])):
          if row in [0, len(board) - 1] or col in [0, len(board[row]) - 1]:
            if board[row][col] == "O":
              mark(row, col, dont_flip)
          
      for row in range(len(board)):
        for col in range(len(board[0])):
          if board[row][col] == "O" and (row, col) not in dont_flip:
            board[row][col] = "X"