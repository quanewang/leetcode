class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)
        t = []
        for i in range(0, k):
            x0, y0 = self.get(m, n, i)
            val = grid[x0][y0]
            j = i + k
            while j < m * n + k:
                x1, y1 = self.get(m, n, j)
                if j < m * n:
                    tmp = grid[x1][y1]
                    grid[x1][y1] = val
                    val = tmp
                else:
                    t.append((x1, y1, val))
                j = j + k
        for x1, y1, val in t:
            grid[x1][y1] = val
        return grid

    def get(self, m, n, i):
        if i >= m * n:
            return self.get(m, n, i - (m * n))
        else:
            return i / n, i % n

"""
Your input
[[1,2,3],[4,5,6],[7,8,9]]
1
Output
[[9,1,2],[3,4,5],[6,7,8]]
Expected
[[9,1,2],[3,4,5],[6,7,8]]

[[1],[2],[3],[4],[7],[6],[5]]
23
"""