class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l=[[0]*n for i in range(n)]
        r=c=di=0
        visited=[[False]*n for _ in range(n)]
        dr=[0,1,0,-1]
        dc=[1,0,-1,0]
        for i in range(n*n):
            l[r][c]=i+1
            
            visited[r][c]=True
            cr,cc=r+dr[di],c+dc[di]
            if(0<=cc<n and 0<=cr<n and not visited[cr][cc]):
                r,c=cr,cc
            else:
                di=(di+1)%4
                r,c=r+dr[di],c+dc[di]
        return l
