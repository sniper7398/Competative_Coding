class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        ans = nums[k-1]
        return ans
        # tc= O(nlogn) 
