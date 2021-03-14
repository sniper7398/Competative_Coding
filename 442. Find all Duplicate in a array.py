class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict = {}
        res = []
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for j in dict:
            if dict[j] > 1:
                res.append(j)
        return res        
