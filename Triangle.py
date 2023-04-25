class Solution(object):
    def minimumTotal(self, triangle):
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i-1][j - (j==i)], triangle[i-1][j - (j>0)])

        return min(triangle[-1])
