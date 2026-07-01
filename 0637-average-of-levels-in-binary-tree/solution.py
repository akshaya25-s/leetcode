# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:        
        r=[]
        if not root:
            return r
        q=collections.deque()
        q.append(root)
        while q:
            s_level=[]
            for i in range(len(q)):
                node=q.popleft()
                s_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            s=sum(s_level)/len(s_level)
            r.append(s)
        return r
