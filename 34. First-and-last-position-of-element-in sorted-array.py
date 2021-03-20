class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i]==target:
                l = i
                break
        else:
            return [-1, -1]
        for j in range(n-1,-1,-1):
            if nums[j] == target:
                r = j
                break
        return [l, r]     
                
