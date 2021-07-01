class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        c = [1]*n #ensuring everyone get atleast one candy
        
        #traversing left to right
        for i in range(n-1):
            if ratings[i]<ratings[i+1]:
                c[i+1] = max(c[i] + 1, c[i+1])
                
        
        #traversing right to left        
        for i in range(n-2, -1, -1):
            if ratings[i+1]<ratings[i]:
                c[i] = max(c[i], c[i+1]+1)
                
        return sum(c)     
