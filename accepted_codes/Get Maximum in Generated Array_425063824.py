class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        l=[0]*(n+1)
        for i in range(n+1):
            if(i==0):
                l[i]=0
            elif(i==1):
                l[i]=1
            elif(i%2==0 and i!=0):
                l[i]=l[i//2]
            elif(i%2!=0 and i!=1):
                l[i]=l[i//2]+l[(i//2)+1]
        return max(l)
