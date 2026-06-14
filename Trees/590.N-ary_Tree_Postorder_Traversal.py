"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        postOrder = []

        def post(current):
            if current is None:
                return
            if current.children:
                for child in current.children:
                    post(child)
            
            postOrder.append(current.val)

        post(root)
        return postOrder
