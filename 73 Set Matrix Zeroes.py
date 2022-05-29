# O(1) Space, O(mn) Time
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Using the 1st row and col to store if the row/col
        # needs to be zeroed. The overlapping mat[0][0] can
        # be stored in a variable
        rows, cols = len(matrix), len(matrix[0])
        # for overlapping mat[0][0] pos
        firstRowZero = False

        # determine which cols and rows need to be zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # mark first corresponding row/col value to be 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        firstRowZero = True
                    matrix[0][c] = 0
        
        # set cells to zero, except first row/col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # zero 1st row
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # zero 1st col
        if firstRowZero:
            for c in range(cols):
                matrix[0][c] = 0            

