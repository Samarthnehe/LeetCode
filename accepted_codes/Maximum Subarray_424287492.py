class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max=nums[0]
        global_max=nums[0]
        for i in range(1,len(nums)):
            curr_max=max(nums[i],curr_max+nums[i])
            if(curr_max>global_max):
                global_max=curr_max
        return global_max
        
