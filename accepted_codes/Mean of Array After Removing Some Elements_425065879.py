import numpy as np
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        x=len(arr)
        perc=round(x/20)
        arr.sort()
        y=x-(perc)
        arr=arr[perc:y]
        return np.mean(arr)
        
