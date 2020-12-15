class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l=[0]*len(code)
        if k==0:
            return l
        elif k>0:
            for i in range(len(code)):
                sum1=0
                for j in range(i+1,i+k+1):
                    sum1=sum1+code[j%len(code)]
                   
                l[i]=sum1
        else:
            for i in range(len(code)-1,-1,-1):
                sum1=0
                for j in range(i-1,(i-1)+k,-1):
                    
                    sum1=sum1+code[j]
                l[i]=sum1
        return l
