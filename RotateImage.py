class Solution(object):
    def rotate(self, matrix):
        # swap rows vertically
        for r in range(len(matrix)//2):
            temp = matrix[r]
            matrix[r] = matrix[len(matrix)-r-1]
            matrix[len(matrix)-r-1] = temp

        # swap diagonally -> swap positions where matrix[row][col] = matrix[col][row]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row == col:
                    break
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp