# https://leetcode.com/problems/spiral-matrix/

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        x = y = 0
        m = len(matrix)
        n = len(matrix[0])
        while x<m-x and y<n-y:
            for j in range(y, n-y):
                result.append(matrix[x][j])
            for i in range(x+1, m-x):
                result.append(matrix[i][n-y-1])
            if (m-x-1>x):
                for j in range(n-y-2, y-1, -1):
                    result.append(matrix[m-x-1][j])
            if (n-y-1>y):
                for i in range(m-x-2, x, -1):
                    result.append(matrix[i][y])
            x += 1
            y += 1
        return result
s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))