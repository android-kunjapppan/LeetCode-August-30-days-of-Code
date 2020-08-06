class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set(nums)
        for number in unique:
            count = nums.count(number)
            if count==1:
                return number
        
        
    
        
