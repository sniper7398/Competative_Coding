class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        t= 0  #top
        b= n-1 #bottom
        l = 0 #left
        r = n-1  #right
        matrix = [[n*n]*n for _ in range(n) ]
        d = 0
        c = 1
        while l<=r and t<=b:
            if d == 0:
                for i in range(l,r+1):
                    matrix[t][i] = c
                    c += 1
                t +=1
                d = 1
                
            elif d == 1:   
                for i in range(t,b+1):
                    matrix[i][r] = c
                    c += 1
                r -=1
                d = 2  
                
            elif d == 2:
                for i in range(r,l-1,-1):
                    matrix[b][i] = c
                    c += 1
                b -=1
                d = 3
                
            elif d == 3:
                for i in range(b,t-1,-1):
                    matrix[i][l] = c
                    c += 1
                l +=1
                d = 0
        return matrix
