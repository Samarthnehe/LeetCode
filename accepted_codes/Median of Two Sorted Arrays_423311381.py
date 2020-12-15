class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final=nums1+nums2
        final.sort()
       
        if ((len(final)%2)==0):
            med=(final[len(final)//2]+final[(len(final)//2)-1])/2
        else:
            med=final[(len(final)//2)]
        return med
