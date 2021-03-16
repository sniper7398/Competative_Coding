class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        l = 0
        r = n-1
        left_max = 0
        right_max = 0
        while l<=r:
            if height[l] <= height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                    l += 1
                else:
                    res += left_max-height[l]
                    l += 1
            else:
                if height[r]>=right_max:
                    right_max = height[r]
                    r -= 1
                else:
                    res += right_max-height[r]
                    r -= 1
        return res            
        
