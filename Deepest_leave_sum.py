Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#ans = [0]
#maxdepth = [-(2**32)]
class Solution:
    def __init__(self):
        self.ans = [0]     # This is init for each test case.
        self.maxdepth = [-(2**32)]
    
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self.helper(root, 0)
    
    def helper(self, node, level):
        if node == None:
            return 
        if (level > self.maxdepth[0]):
            self.ans[0] = node.val
            self.maxdepth[0] = level
        elif (level == self.maxdepth[0]):
            self.ans[0] = self.ans[0] + node.val
            
        self.helper(node.left, level+1)
        self.helper(node.right, level+1)
        
        return self.ans[0]
    
