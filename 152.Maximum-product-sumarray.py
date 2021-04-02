import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_forw = -sys.maxsize-1
        max_back = -sys.maxsize-1
        iszero = False
        curr_max = 1
        
        
        for i in range(n):
            curr_max = curr_max*nums[i]
            if curr_max == 0:
                iszero = True
                curr_max = 1
                continue
            if curr_max>max_forw:
                max_forw = curr_max
        curr_max =1
        for i in range(n-1,-1,-1):
            curr_max = nums[i]*curr_max
            if curr_max == 0:
                iszero = True
                curr_max = 1
                continue
            if curr_max > max_back:
                max_back = curr_max
        res = max(max_forw, max_back)
        if iszero == True:
            res = max(res, 0)
        return res    
                
