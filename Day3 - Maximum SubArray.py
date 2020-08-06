class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        sub_sum = nums[0]
        
        for i in range(1, len(nums)):
            sub_sum = max(nums[i], nums[i]+sub_sum)
            sum = max(sum, sub_sum)
            
        return sum
        
