# https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        b = 0
        e = m - 1
        while b < e:
            m = (b + e) / 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                e = m - 1
            elif matrix[m][n - 1] >= target:
                b = e = m
            else:
                b = m + 1
        if b == e:
            return self.search(matrix, b, target)
        return False

    def search(self, matrix, k, target):
        b = 0
        e = len(matrix[0]) - 1
        while b < e:
            m = (b + e) / 2
            if matrix[k][m] == target:
                return True
            elif matrix[k][m] < target:
                b = m + 1
            else:
                e = m - 1
        if b == e and matrix[k][b] == target:
            return True
        return False

