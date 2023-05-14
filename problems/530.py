from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> float:
        min_val = float('inf')
        curr_val = None
        def inorderTraversal(node):
            nonlocal curr_val, min_val
            if node is None:
                return
            inorderTraversal(node.left)
            if curr_val is not None and curr_val !=node.val:
                diff_val = node.val - curr_val
                curr_val = node.val
                min_val = min(min_val, diff_val)
            elif curr_val is None:
                curr_val = node.val
            inorderTraversal(node.right)
        inorderTraversal(root)

        return min_val
