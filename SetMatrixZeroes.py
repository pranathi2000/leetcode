class Solution(object):
    def setZeroes(self, matrix):
        rows = []
        cols = []
        for row in range(len(matrix)):
            if 0 in matrix[row]:
                rows.append(row)
                index = 0
                while 0 in matrix[row][index:]:
                    cols.append(matrix[row].index(0,index))
                    index = matrix[row].index(0,index) + 1

        for r in rows:
            matrix[r] = [0] * len(matrix[r])

        for c in cols:
            for s in range(len(matrix)):
                matrix[s][c] = 0

        return matrix

