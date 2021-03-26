class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = 0
        maxi = nums[0]
        for num in nums:
            sums+=num
            maxi = max(sums, maxi)
            if sums<0:
                sums = 0
        return maxi        
