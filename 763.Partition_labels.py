class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        ans = []
        arr = {c: i for i, c in enumerate(S)} #to get last index of char in S
        end=start=0
        for i, c in enumerate(S):
            end = max(end, arr[c])
            if i==end:
                ans.append(i-start+1)
                start = i+1
        return ans        
