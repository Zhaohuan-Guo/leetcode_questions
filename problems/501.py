from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        curr_val = None
        max_count = 0
        curr_count = 1
        modes = []

        def count(val):
            nonlocal curr_val, max_count, curr_count
            if val == curr_val:
                curr_count += 1
            else:
                curr_val = val
                curr_count = 1
            if curr_count > max_count:
                max_count = curr_count
                modes.clear()
                modes.append(curr_val)
            elif curr_count == max_count:
                modes.append(curr_val)

        def inorderTraversal(node):
            if node is None:
                return
            inorderTraversal(node.left)
            count(node.val)
            inorderTraversal(node.right)

        inorderTraversal(root)
        return modes