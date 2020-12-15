class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        arr=[]
        max_area=0
        if(len(heights)==1):
            return heights[0]
        for j in range(len(heights)):
            if j==len(heights)-1 or heights[j]>heights[j+1]:
                min_height=heights[j]
                for i in range(j,-1,-1):
                    min_height=min(min_height,heights[i])
                    width=j-i+1
                    area=min_height*width
                    if(area>max_area):
                        max_area=area;
        return max_area
        
