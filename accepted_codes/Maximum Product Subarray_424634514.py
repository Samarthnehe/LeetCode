class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=nums[0]
        minimum=nums[0]
        result=maximum
        for i in range(1,len(nums)):
            curr=nums[i]
            maximum,minimum=max(curr,curr*maximum,curr*minimum), min(curr,curr*maximum,curr*minimum)
            result=max(result,maximum)
        return result
