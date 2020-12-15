class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=0
        r=len(mat)
        c=len(mat[0])
        for i in range(r):
            for j in range(c):
                if(i==j):
                  
                    sum1+=mat[i][j]
                elif(i+j==r-1):
                    
                    sum1+=mat[i][j]
        return sum1
