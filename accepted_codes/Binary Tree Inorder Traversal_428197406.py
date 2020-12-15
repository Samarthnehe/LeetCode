# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # @lru_cache(maxsize=None)
        def left(root,res):
            if not root: return res
            if root.left:
                left(root.left,res)
            res.append(root.val)
            if root.right:
                left(root.right,res)
        res=[]
        left(root,res)
        return res
