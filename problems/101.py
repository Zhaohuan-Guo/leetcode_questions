# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_mirror(l, r):
            if not l and not r:
                return True
            if not l or not r or l.val != r.val:
                return False
            return check_mirror(l.left, r.right) and check_mirror(l.right, r.left)
        return check_mirror(root.left, root.right)