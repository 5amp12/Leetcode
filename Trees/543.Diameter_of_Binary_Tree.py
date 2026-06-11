# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.biggestDia = 0

        def binTree(root):
            if not root:
                return 0

            print(root.val)
            left = binTree(root.left)
            right = binTree(root.right)

            self.biggestDia = max(self.biggestDia, left + right)
            return 1 + max(left, right)
        
        binTree(root)

        return self.biggestDia
