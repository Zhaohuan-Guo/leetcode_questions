# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def get_height(node):
            if node is None:
                return 0
            left_height = 0 if not node.left else get_height(node.left)
            right_height = 0 if not node.right else get_height(node.right)
            return max(left_height, right_height) + 1

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            if abs(get_height(root.left) - get_height(root.right)) > 1:
                return False
            else:
                return True
'''
Given a binary tree, determine if it is 
height-balanced.
Height-Balanced
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
'''