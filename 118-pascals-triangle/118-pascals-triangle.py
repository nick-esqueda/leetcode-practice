class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        [
              [1]
             [1,1]
            [1,2,1]
           [1,3,3,1]
          [1,4,6,4,1]
        ]
        
        to calculate the value at a given index in any row, sum the previous row's (i - 1) + (i) together
        the first and last num will always be 1
        """
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        tab = [[1], [1, 1]]
        
        for i in range(2, numRows):
            row = [1] * (i + 1)
            for j in range(1, len(row) - 1):
                row[j] = tab[i - 1][j - 1] + tab[i - 1][j]
            tab.append(row)
        return tab
            