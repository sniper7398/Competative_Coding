class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        if l==0:
            return 0
        elif s[l]==" ":
            return 0
