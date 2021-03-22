class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tot = set(range(1, n+1))
        cur = set(nums)
        return (tot-cur)
