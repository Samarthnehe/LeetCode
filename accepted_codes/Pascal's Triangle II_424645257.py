class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l1=[[1]]
        l=[]
        
        for i in range(1,rowIndex+1):
            l.append(1)
            for j in range(0,i-1):
                l.append(l1[i-1][j]+l1[i-1][j+1])
            l.append(1)
            l1.append(l)
            l=[]
        return l1[-1]
        
