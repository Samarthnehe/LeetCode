class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or max(nums)<0: return 1
        for i in range(1,max(nums)+2):
            if i not in nums:
                return i
                break
            
