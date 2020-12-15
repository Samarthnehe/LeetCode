class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res=[]
        for i in intervals:
            if not res or res[-1][1]<i[0]:
                res.append(i)
            else:
                res[-1][1]=max(res[-1][1],i[1])
        return res
