class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='1':
                    count += 1
                    self.bfs(grid, i, j)
        return count
    
    def bfs(self,grid, i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.bfs(grid, i+1, j)
        self.bfs(grid, i-1, j)
        self.bfs(grid, i, j+1)
        self.bfs(grid, i, j-1)
