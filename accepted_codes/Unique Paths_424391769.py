class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0 for i in range (n)] for j in range(m)]
        for i in range (m):
            for j in range (n):
                if(i == 0 or j == 0):
                    path[i][j] = 1
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]
        return path[m-1][n-1];
