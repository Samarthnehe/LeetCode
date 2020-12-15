class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R=len(matrix)
        C=len(matrix[0])
        visited=[[False]*C for m in range(R)]
        dr=[0,1,0,-1]
        dc=[1,0,-1,0]
        c=r=di=0
        final=[]
        for i in range(R*C):
            final.append(matrix[r][c])
            visited[r][c]=True
            cr,cc=r+dr[di],c+dc[di]
            if (0<=cc<C and 0<=cr<R and not visited[cr][cc]):
                r,c=cr,cc
            else:
                di=(di+1)%4
                r,c=r+dr[di],c+dc[di]
        return final
