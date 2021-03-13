class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        dp = 0
        for i in range(2,n):
            if (nums[i]-nums[i-1] == nums[i-1]-nums[i-2]):
                
                dp = 1+dp
                s += dp
            else:
                dp = 0
        return s
