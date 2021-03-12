from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in collections.Counter(s).values():
            res += i//2*2
            if res % 2 ==0 and i % 2 == 1:
                res += 1
        return res        
      
      #input = abccccdd
      #output = 7
