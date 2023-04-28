class Solution(object):
    def spiralOrder(self, matrix):
        m,n = len(matrix), len(matrix[0])
        leftBound, rightBound, topBound, bottomBound = 0, n-1, 0, m-1
        order = []

        while leftBound <= rightBound and topBound <= bottomBound:
            for i in range(leftBound, rightBound+1):
                order.append(matrix[topBound][i])
            topBound+=1

            for j in range(topBound, bottomBound+1):
                order.append(matrix[j][rightBound])
            rightBound-=1

            for k in range(rightBound, leftBound-1, -1):
                order.append(matrix[bottomBound][k])
            bottomBound-=1

            for p in range(bottomBound, topBound-1, -1):
                order.append(matrix[p][leftBound])
            leftBound+=1

        return order[0:m*n]