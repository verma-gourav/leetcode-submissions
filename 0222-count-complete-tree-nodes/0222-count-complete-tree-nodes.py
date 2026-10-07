# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        left_depth = 0
        left_node = root
        while left_node:
            left_depth += 1
            left_node = left_node.left
        
        right_depth = 0
        right_node = root
        while right_node:
            right_depth += 1
            right_node = right_node.right
        
        # if height match, its perfect binary tree
        if left_depth == right_depth:
            return (2 ** left_depth) - 1
        
        # if height doesnt match, recurssion on left and right
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)