# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        c=root
        while c:
            if c.left:
                p=c.left
                while p.right:
                    p=p.right
                p.right=c.right
                c.right=c.left
                c.left=None
            c=c.right
        
        
