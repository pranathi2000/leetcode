class Solution(object):
    def searchMatrix(self, matrix, target):
        # element i is matrix[i//m][i%m]

        m, n = len(matrix[0]), len(matrix)
        left, right = 0, m*n-1
        while left < right:
            i = (right+left)//2
            if matrix[i//m][i%m] == target:
                return True
            elif matrix[i//m][i%m] < target:
                left = i+1
            elif matrix[i//m][i%m] > target:
                right = i
        return matrix[left//m][left%m] == target