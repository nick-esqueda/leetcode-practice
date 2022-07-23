class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        [[1, 2]]
        """
        left, top = 0, 0
        right, bottom = len(matrix[0]) - 1, len(matrix) - 1
        
        output = []
        while top <= bottom and left <= right:
            # top
            for c in range(left, right + 1):
                output.append(matrix[top][c])
            top += 1

            # right
            for r in range(top, bottom + 1):
                output.append(matrix[r][right])
            right -= 1

            # bottom
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    output.append(matrix[bottom][c])
                bottom -= 1

            # left
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    output.append(matrix[r][left])
                left += 1
        return output