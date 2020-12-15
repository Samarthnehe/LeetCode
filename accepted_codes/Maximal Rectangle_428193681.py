class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        h=[0]*len(matrix[0])
        max_area=0
        def findArea(h):
            n=len(h)
            maxy=0
            for i in range(n):
                if i==n-1 or h[i]>h[i+1]:
                    min_height=h[i]
                    for j in range(i,-1,-1):
                        min_height=min(min_height,h[j])
                        width=i-j+1
                        area=min_height*width
                        if(area>maxy):
                            maxy=area
            return maxy
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]=="0"):
                    h[j]=0
                else:
                    h[j]+=1
           
            max_area=max(max_area,findArea(h))  
        return max_area
