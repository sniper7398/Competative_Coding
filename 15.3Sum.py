class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        nums.sort()
        res = []
        for i in range(n-2):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                l = i+1
                h = n-1
                sums = 0 - nums[i]
                while l<h:
                    if nums[l] + nums[h] == sums:
                        res.append([nums[i],nums[l],nums[h]])
                        while l<h and nums[l]==nums[l+1]:
                            l += 1
                        while l<h and nums[h] == nums[h-1]:
                            h -= 1
                        l += 1
                        h -= 1
                    elif nums[l]+nums[h]<sums:
                        l += 1
                    else:
                        h -= 1
        return res           
                
