# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        rs_list = []
        help_list = []

        while node or help_list:
            while node:
                help_list.append(node)
                node = node.left
            node = help_list.pop()
            rs_list.append(node.val)
            node = node.right

        return rs_list