# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        value = root.val
        def allSameNumber(root):
            nonlocal value
            if root is None:
                return True
            
            if root.val != value:
                return False
            
            return allSameNumber(root.left) and allSameNumber(root.right)
        
        return allSameNumber(root)