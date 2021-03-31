class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums%2 != 0:
            return False
        n = len(nums)
        m = sums//2
        M = [[True for i in range(n + 1)]
            for j in range(m + 1)]#[[0]*(n+1)]*(m+1)
        
        for i in range(n+1):
            M[0][i] == True
            
        for i in range(1, m+1):
            M[i][0] = False
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                M[i][j] = M[i][j-1]
                if i >= nums[j-1]:
                    M[i][j] = (M[i][j] or M[i-nums[j-1]][j-1])
        return M[m][n]            
